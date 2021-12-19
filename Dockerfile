from alpine:latest

RUN apk add --no-cache python3 py3-pip

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir requirements.txt
