#!/bin/sh

if [ -d /deployment ];
then
	echo "Mapping deployed wars"
	rm -rf /usr/local/tomcat/webapps
	ln -s /deployment /usr/local/tomcat/webapps
fi

