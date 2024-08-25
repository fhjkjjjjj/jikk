# Use the Cypress base image with browsers
FROM cypress/browsers:latest

# Set environment variable for the port
ARG PORT=443
ENV PORT=${PORT}

# Install Python and pip
RUN apt-get update && \
    apt-get install -y python3-pip python3-venv

# Create a virtual environment
RUN python3 -m venv /env

# Install Python dependencies into the virtual environment
COPY requirements.txt .
RUN /env/bin/pip install -r requirements.txt

# Copy application code
COPY . /app

# Set the working directory
WORKDIR /app

# Expose the port
EXPOSE 443

# Use the virtual environment's Python to run the app
CMD /env/bin/uvicorn main:app --host 0.0.0.0 --port $PORT
