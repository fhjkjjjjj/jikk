ARG PORT=443
FROM cypress/browsers:latest
RUN apt-get update && \
    apt-get install -y python3 python3-pip
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . /app
WORKDIR /app
CMD uvicorn main:app --host 0.0.0.0 --port $PORT
