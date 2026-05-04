# mlops_chatbot
mlops chatbot assgn

# MLOps Chatbot: Automated CI/CD Deployment to Windows

This project demonstrates a complete MLOps pipeline for deploying a Groq-powered chatbot application. It utilizes GitHub Actions and a self-hosted runner to automate the containerization and deployment process directly onto a Windows-based environment.

## Project Overview
The goal of this project was to establish a seamless "Push-to-Deploy" workflow. Every time code is pushed to the `main` branch, a GitHub Action triggers a build process on a local Windows machine, updates the Docker image, and restarts the application container.

### Key Technologies
* **Application:** Python, Streamlit, Groq API
* **Containerization:** Docker Desktop
* **Orchestration:** GitHub Actions
* **Runner:** GitHub Self-Hosted Runner (Windows)
* **Scripting:** PowerShell

---

## What We Accomplished

1.  **Application Development:** Created a chatbot interface using Streamlit powered by the Groq LLM.
2.  **Dockerization:** Wrote a `Dockerfile` to package the app and its dependencies into a lightweight, portable image.
3.  **CI/CD Configuration:** Created a `deploy.yml` workflow that:
    * Detects code changes on GitHub.
    * Communicates with a local Windows machine.
    * Bypasses Windows PowerShell Execution Policies (`UnauthorizedAccess` errors) using direct command string execution.
    * Automates the `docker stop`, `docker build`, and `docker run` cycle.
4.  **Self-Hosted Runner Setup:** Configured a local machine as a GitHub runner to bridge the gap between the cloud repository and local hardware.

---

## How to Execute This Project

### 1. Prerequisites
* **GitHub Account:** A repository containing your code.
* **Docker Desktop:** Installed and running on Windows.
* **Git:** Installed on your local machine.

### 2. Setup GitHub Self-Hosted Runner
1.  Go to your GitHub Repository -> **Settings** -> **Actions** -> **Runners**.
2.  Click **New self-hosted runner** and select **Windows**.
3.  Follow the download and extraction instructions provided by GitHub.
4.  In an **Administrator PowerShell** window, run the `./config.cmd` command provided by GitHub.
5.  Start the runner by executing:
    ```powershell
    ./run.cmd
    ```
    *Keep this window open to listen for deployment jobs.*

### 3. Configure GitHub Secrets
Go to **Settings** -> **Secrets and variables** -> **Actions** and add any necessary environment variables (e.g., `GROQ_API_KEY`) if your app requires them at runtime.

### 4. Deploying the Workflow
The `deploy.yml` file is configured to run on a `self-hosted` label. To deploy:
1.  Ensure your `deploy.yml` is located in `.github/workflows/`.
2.  Push your changes:
    ```powershell
    git add .
    git commit -m "Deploying app via self-hosted runner"
    git push origin main
    ```
3.  Monitor the **Actions** tab on GitHub. The runner will execute the PowerShell commands to build and run the Docker container.

### 5. Access the App
Once the workflow shows a green checkmark, the application will be live on your local machine at:
**[http://localhost:8501](http://localhost:8501)**

---

## Troubleshooting Note
If you encounter `UnauthorizedAccess` or `Execution_Policies` errors on Windows, the workflow is designed to use the `-ExecutionPolicy Bypass` flag. Ensure you are running the GitHub Runner as an **Administrator** to give it sufficient permissions to manage Docker containers.
