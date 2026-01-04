# Use a lightweight Python base image
FROM python:3.11-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY ./app .

# Expose the ports the app runs on
EXPOSE 8000
EXPOSE 8501

# Copy the startup script
COPY start.sh .
RUN chmod +x start.sh

# Command to run the application
ENTRYPOINT ["./start.sh"]
