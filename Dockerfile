FROM python:3-alpine

RUN mkdir -p /src
WORKDIR /src

COPY requirements.txt /src

RUN pip install -r requirements.txt

COPY . /src