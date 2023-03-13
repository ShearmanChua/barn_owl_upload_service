FROM python:3.8.15-slim-buster

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

RUN pip install -U pip

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir /upload_service && mkdir /upload_service/src 
WORKDIR /upload_service