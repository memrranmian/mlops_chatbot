FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install streamlit groq
EXPOSE 8501
# Note: Streamlit uses 8501 by default; your image mentions 5000. 
# We'll stick to 8501 for Streamlit.
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]