# image name: opencv-python
# VERSION     2

FROM python:3.9.6-buster
LABEL maintainer="bo.yan@csiro.au"

ADD requirements.txt /app/requirements.txt

# ImportError: libGL.so.1: cannot open shared object file: No such file or directory solution
RUN apt update && apt install -y libgl1-mesa-glx

RUN pip install -r /app/requirements.txt

