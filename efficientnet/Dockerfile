FROM nvcr.io/nvidia/pytorch:21.07-py3

RUN apt-get update && apt-get install -y git\
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV WORK_BASE /opt/efficientnet
# Create a working directory
RUN mkdir -p "$WORK_BASE"
WORKDIR "$WORK_BASE"

# Install Efficientnet from the commit #7e8b0d3
RUN git clone https://github.com/lukemelas/EfficientNet-PyTorch "$WORK_BASE" \
    && git checkout 7e8b0d3

RUN pip install -e .