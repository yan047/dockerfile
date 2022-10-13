FROM yan047/mvt-mmclassification:1

LABEL maintainer="bo.yan@csiro.au"

RUN apt -qq update && apt -qq -y install ffmpeg

ADD requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

EXPOSE 5000