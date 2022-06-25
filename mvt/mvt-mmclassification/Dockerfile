FROM yan047/mvt-yolox:1

LABEL maintainer="bo.yan@csiro.au"


# step 1, install openmim 0.1.6, this will down-grade click-8.0.3 to click-7.1.2
RUN pip install openmim

# step 2, use mim to install mmcv-full 1.5.0, addict-2.4.0, yapf-0.32.0
# mmclassification requires mmcv>=1.4.2, <=1.5.0
RUN mim install mmcv-full==1.5.0

WORKDIR "$WORK_BASE"
RUN git clone https://github.com/open-mmlab/mmclassification.git --branch v0.20.1
WORKDIR "$WORK_BASE/mmclassification"

RUN pip install -v -e .


