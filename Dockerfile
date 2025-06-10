FROM python:3.6-slim

RUN pip3 install --upgrade pip

ENV TZ=Asia/Seoul

WORKDIR /app

RUN python3 setup.py install

