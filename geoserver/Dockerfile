# Version: 1
# Name: geoserver-2.16

FROM yan047/geoserver-prep:1

MAINTAINER Bo Yan (boyan.au@gmail.com)

# modified from https://hub.docker.com/r/oscarfonts/geoserver/dockerfile

ENV GEOSERVER_VERSION 2.16.0
ENV GEOSERVER_DATA_DIR /var/local/geoserver
ENV GEOSERVER_INSTALL_DIR /usr/local/geoserver

# GeoServer
ADD conf/geoserver.xml /usr/local/tomcat/conf/Catalina/localhost/geoserver.xml
RUN mkdir ${GEOSERVER_DATA_DIR} \
	&& mkdir ${GEOSERVER_INSTALL_DIR} \
	&& cd ${GEOSERVER_INSTALL_DIR} \
	&& wget http://sourceforge.net/projects/geoserver/files/GeoServer/${GEOSERVER_VERSION}/geoserver-${GEOSERVER_VERSION}-war.zip \
	&& unzip geoserver-${GEOSERVER_VERSION}-war.zip \
	&& unzip geoserver.war \
	&& mv data/* ${GEOSERVER_DATA_DIR} \
	&& rm -rf geoserver-${GEOSERVER_VERSION}-war.zip geoserver.war target *.txt

# Install extensions
RUN wget https://sourceforge.net/projects/geoserver/files/GeoServer/${GEOSERVER_VERSION}/extensions/geoserver-${GEOSERVER_VERSION}-csw-plugin.zip -P ${GEOSERVER_INSTALL_DIR} \
    && wget https://sourceforge.net/projects/geoserver/files/GeoServer/${GEOSERVER_VERSION}/extensions/geoserver-${GEOSERVER_VERSION}-inspire-plugin.zip -P ${GEOSERVER_INSTALL_DIR} \
    && wget https://build.geoserver.org/geoserver/2.16.x/community-2019-09-23/geoserver-2.16-SNAPSHOT-csw-iso-plugin.zip -P ${GEOSERVER_INSTALL_DIR}


RUN unzip -qo ${GEOSERVER_INSTALL_DIR}/geoserver-${GEOSERVER_VERSION}-csw-plugin.zip -d ${GEOSERVER_INSTALL_DIR}/WEB-INF/lib \
    && unzip -qo ${GEOSERVER_INSTALL_DIR}/geoserver-${GEOSERVER_VERSION}-inspire-plugin.zip -d ${GEOSERVER_INSTALL_DIR}/WEB-INF/lib \
    && unzip -qo ${GEOSERVER_INSTALL_DIR}/geoserver-2.16-SNAPSHOT-csw-iso-plugin.zip -d ${GEOSERVER_INSTALL_DIR}/WEB-INF/lib \
    && rm ${GEOSERVER_INSTALL_DIR}/*.zip

# Enable CORS
RUN sed -i '\:</web-app>:i\
<filter>\n\
    <filter-name>CorsFilter</filter-name>\n\
    <filter-class>org.apache.catalina.filters.CorsFilter</filter-class>\n\
    <init-param>\n\
        <param-name>cors.allowed.origins</param-name>\n\
        <param-value>*</param-value>\n\
    </init-param>\n\
    <init-param>\n\
        <param-name>cors.allowed.methods</param-name>\n\
        <param-value>GET,POST,HEAD,OPTIONS,PUT</param-value>\n\
    </init-param>\n\
</filter>\n\
<filter-mapping>\n\
    <filter-name>CorsFilter</filter-name>\n\
    <url-pattern>/*</url-pattern>\n\
</filter-mapping>' ${GEOSERVER_INSTALL_DIR}/WEB-INF/web.xml

# Tomcat environment
ENV CATALINA_OPTS "-server -Djava.awt.headless=true \
	-Xms768m -Xmx1560m -XX:+UseConcMarkSweepGC -XX:NewSize=48m \
	-DGEOSERVER_DATA_DIR=/var/local/geoserver"

ADD start.sh /usr/local/bin/start.sh
CMD start.sh

EXPOSE 8080