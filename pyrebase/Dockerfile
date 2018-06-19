FROM python:3.6.5-stretch

MAINTAINER "boyan.au@gmail.com"

ENV DEBIAN_FRONTEND noninteractive

RUN pip3 install django && \ 
	pip3 install djangorestframework && \ 
	pip3 install pymysql && \
	pip3 install pyrebase

RUN mkdir -p /app
ADD runapp.sh /app
RUN cd /app && chmod a+x runapp.sh

EXPOSE 8000 8080
