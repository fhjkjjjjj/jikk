ARG PORT=443
FROM cypress/browsers:latest
RUN echo $(python3 -m site --user-base)
COPY requirements.txt .
ENV PATH /home/root/.local/bin:${PATH}
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install -r requirements.txt
COPY . /app
CMD uvicorn main:app --host 0.0.0.0 --port $PORT
