FROM nvcr.io/nvidia/pytorch:22.02-py3

LABEL maintainer="bo.yan@csiro.au"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt -qq update && apt -qq -y install libgl1-mesa-glx ffmpeg \
    && apt-get clean

ENV WORK_BASE /install
WORKDIR "$WORK_BASE"

# Install YOLOX
RUN git clone https://github.com/CindyXin007/tracking_yolox.git 

WORKDIR "$WORK_BASE/tracking_yolox"

RUN git checkout 0.4.0
RUN pip3 install -v -e .
