# Version: 1
# Name: geoserverharvester

FROM python:3.7-buster

MAINTAINER Bo Yan (boyan.au@gmail.com)

ENV WORK_DIR /var/geoharvester
RUN mkdir ${WORK_DIR} \
	&& mkdir ${WORK_DIR}/output 

ADD Dockerfile /etc/Dockerfile
ADD geoharvester ${WORK_DIR} 

WORKDIR ${WORK_DIR}

RUN pip install -r ${WORK_DIR}/install.txt

CMD python main.py ${GEOSERVER} ${WORK_DIR}/output
