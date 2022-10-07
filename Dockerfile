# Change this file as necessary
FROM python:3.8-slim-buster

WORKDIR /app
# This path must exist as it is used as a mount point for testing
# Ensure your app is loading files from this location
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3","-m","flask", "--app","main","run", "--host=0.0.0.0", "--port=8279" ]


