# Use the Cypress base image with browsers
FROM cypress/browsers:latest

# Set environment variable for the port
ARG PORT=443

# Set environment variable for Python user base directory
ENV PYTHONUSERBASE=/home/root/.local

# Update package lists and install Python and pip
RUN apt-get update && \
    apt-get install -y python3-pip

# Install Python dependencies
COPY requirements.txt .
RUN pip3 install --user -r requirements.txt

# Copy application code
COPY . /app

# Set the working directory
WORKDIR /app

# Expose the port
EXPOSE 443

# Define the command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "$PORT"]
