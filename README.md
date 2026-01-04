# AI Travel Agent

This is a proof-of-concept AI-powered travel agent using gemini 2.5 API. It provides a web-based chat interface for users to interact with an AI to plan their travels.

The application is built with a Python backend using FastAPI and a frontend using Streamlit. The entire application is containerized with Docker for easy setup and deployment.

## Project Structure

```
.
├── app/
│   ├── main.py        # FastAPI backend that serves the API
│   ├── ui.py          # Streamlit frontend for the user interface
│   ├── run_agent.py   # Handles the core logic for the AI agent
│   └── search.py      # Provides search functionalities for the agent
├── Dockerfile         # Defines the instructions to build the Docker image
├── requirements.txt   # Lists the Python dependencies for the project
├── start.sh           # A startup script to run both the backend and frontend in the container
└── README.md          # This file
```

## Getting Started

To get the application running, you will need Docker installed and running on your machine.

1.  **Build the Docker Image**

    Open your terminal and run the following command from the root of the project directory:
    ```bash
    docker build -t ai-travel-agent .
    ```

2.  **Run the Docker Container**

    Once the image is built, run the following command to start the container. This will start both the backend and the UI.
    ```bash
    docker run -p 8000:8000 -p 8501:8501 ai-travel-agent
    ```

3.  **Access the Application**

    You can now access the Streamlit UI by navigating to the following URL in your web browser:
    [http://localhost:8501](http://localhost:8501)

The backend API will be accessible at `http://localhost:8000`.