import streamlit as st
from groq import Groq

# 1. Page Configuration
st.set_page_config(page_title="Groq FastChat", page_icon="⚡")
st.title("⚡ Groq FastChat")
st.caption("Powered by Groq LPU™ Inference Engine")

# 2. Sidebar for Configuration
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Enter Groq API Key:", type="password")
    model_option = st.selectbox(
        "Choose a model:",
        ("llama-3.3-70b-versatile", "llama-3.1-8b-instant", "mixtral-8x7b-32768")
    )
    
    if not api_key:
        st.warning("Please enter your API key to start.")
        st.stop()

# 3. Initialize Groq Client
client = Groq(api_key=api_key)

# 4. Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# 5. Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. Chat Input Logic
if prompt := st.chat_input("What's on your mind?"):
    # Add user message to state and display
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate Assistant Response
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        try:
            # Call Groq API with Streaming
            stream = client.chat.completions.create(
                model=model_option,
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            )

            for chunk in stream:
                if chunk.choices[0].delta.content:
                    full_response += chunk.choices[0].delta.content
                    response_placeholder.markdown(full_response + "▌")
            
            response_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            st.error(f"An error occurred: {e}")