#!/bin/sh

# Start the FastAPI backend in the background
uvicorn main:app --host 0.0.0.0 --port 8000 &

# Start the Streamlit frontend
# We use --server.enableCORS=false to avoid potential cross-origin issues when running in a container
streamlit run ui.py --server.port 8501 --server.address 0.0.0.0 --server.enableCORS=false
