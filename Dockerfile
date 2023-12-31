# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Install dependencies
RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0

RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt --timeout=1000

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose the port that the FastAPI application will run on
EXPOSE 8000

# Define environment variables
ENV FASTAPI_HOST=0.0.0.0
ENV FASTAPI_PORT=8000

# Command to run the FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
