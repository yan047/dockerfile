# Modified from https://hub.docker.com/r/ultralytics/yolov5/dockerfile

# image name yan047/yolov5

# Start FROM Nvidia PyTorch image https://ngc.nvidia.com/catalog/containers/nvidia:pytorch
FROM nvcr.io/nvidia/pytorch:20.03-py3

LABEL maintainer="bo.yan@csiro.au"

# get WORK_BASE ready
ENV WORK_BASE /app

RUN mkdir -p "$WORK_BASE"

# ImportError: libGL.so.1: cannot open shared object file: No such file or directory solution
RUN apt update && apt install -y libgl1-mesa-glx

# get yolov5 3.0 release
RUN cd "$WORK_BASE" && git clone https://github.com/ultralytics/yolov5 \
    && cd yolov5 \
    && git checkout tags/v3.0

# set yolov5 as WORKDIR
WORKDIR "$WORK_BASE/yolov5"

RUN pip install -r requirements.txt gsutil

