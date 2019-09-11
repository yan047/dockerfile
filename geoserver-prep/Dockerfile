# Version: 1
# Name: geoserver-prep

FROM tomcat:9-jdk11-adoptopenjdk-hotspot

MAINTAINER Bo Yan (boyan.au@gmail.com)

# install dependencies: Microsoft fonts, libfontconfig1  for the bug https://github.com/AdoptOpenJDK/openjdk-docker/issues/75
RUN apt-get update \
	&& apt-get install -yq --no-install-recommends wget unzip vim ttf-mscorefonts-installer libfontconfig1 \
    && rm -rf /var/lib/apt/lists/*