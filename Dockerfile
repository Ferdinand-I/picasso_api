FROM python:3.11-slim

WORKDIR /app

COPY ./requirements.txt .

RUN pip3 install --upgrade pip

RUN apt-get update -y

RUN apt-get install -y libmagic-dev

RUN pip3 install -r requirements.txt --no-cache-dir

COPY ./picasso_api .