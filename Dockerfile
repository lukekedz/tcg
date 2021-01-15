FROM python:3.7.3

WORKDIR /core
COPY core .
COPY requirements.txt .

RUN pip install -r requirements.txt
