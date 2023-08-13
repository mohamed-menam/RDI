FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN mkdir /RDI


WORKDIR /RDI

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt 
