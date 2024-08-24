ARG PORT=443
FROM cypress/browsers:latest
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install -r requirements.txt
COPY . /app
WORKDIR /app
CMD uvicorn main:app --host 0.0.0.0 --port $PORT
