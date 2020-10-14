FROM yan047/yolov5:v3.0

LABEL maintainer="bo.yan@csiro.au"

RUN apt -qq update && apt -qq -y install ffmpeg

ADD requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

EXPOSE 5000