FROM yan047/mvt-mmclassification:1

LABEL maintainer="bo.yan@csiro.au"

RUN apt -qq update && apt -qq -y install ffmpeg

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -qq update && apt-get -qq -y install ffmpeg libgl1-mesa-glx && \
        apt-get -qq -y autoremove && apt-get -qq -y autoclean

ENV WORK_BASE /install
WORKDIR "$WORK_BASE"
RUN git clone https://github.com/yan073/HINet
WORKDIR "$WORK_BASE/HINet"
RUN git checkout v1 && \
    pip install -r requirements.txt && python setup.py develop --no_cuda_ext

ADD requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

EXPOSE 5000