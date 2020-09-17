FROM yan047/yolov5:v3.0

LABEL maintainer="bo.yan@csiro.au"

RUN pip install colorhash xlrd

RUN apt -qq update && apt -qq -y install ffmpeg

RUN mkdir /data && mkdir /output && mkdir /service

EXPOSE 5000