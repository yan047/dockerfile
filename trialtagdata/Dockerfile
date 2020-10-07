FROM mongo:4.2

LABEL maintainer="bo.yan@csiro.au"

ADD data /docker-entrypoint-initdb.d/

WORKDIR /docker-entrypoint-initdb.d/

RUN gunzip *.gz
