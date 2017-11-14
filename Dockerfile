FROM python:3.5

RUN mkdir /application

RUN apt-get update && apt-get upgrade -y && apt-get install -y npm nodejs-legacy

ADD . /application
RUN chmod +x -R application

RUN pip install -r /application/requirments.txt && cd /application && npm install

VOLUME ["/application"]
WORKDIR /application
ENV PYTHONUNBUFFERED 1