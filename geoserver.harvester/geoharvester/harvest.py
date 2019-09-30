#!python
# coding=utf-8
import os
import sys
import requests
from crawlcsw import CrawlCSW

import logging
import logging.handlers


class GeoServerHarvester:
    def __init__(self, geoserver_url, out_dir, log_file=None, select=None, clean=True):
        # print ('GeoServerHarvester init!') 
        self.logger = logging.getLogger('geoserver_crawler')
        self.logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s - [%(levelname)s] %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)
        self.logger.info("start harvesting %s ...", geoserver_url)

        if not os.path.exists(out_dir):
            os.makedirs(out_dir)

        ccsw = CrawlCSW(geoserver_url, logger=self.logger)
        self._save(out_dir, ccsw.datasets)

    def _save(self, out_dir, isos):
        for iso in isos:
            try:
                filename = iso['id'].replace("/", "_").replace(":", "_")
                filename = filename + ".iso.xml"
                filepath = os.path.join(out_dir, filename)
                self.logger.info("Saving to %s" % filepath)
                with open(filepath, 'wb') as f:
                    f.write(iso['xml'])
                    f.close()
            except KeyboardInterrupt:
                self.logger.info("Caught interrupt, exiting")
                sys.exit(0)
            except BaseException:
                self.logger.exception("Error!")


    def __add_stream_logger(self):
        formatter = logging.Formatter('%(asctime)s - [%(levelname)s] %(message)s')
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def __add_file_logger(self, log_file):
        formatter = logging.Formatter('%(asctime)s - [%(levelname)s] %(message)s')
        fh = logging.handlers.RotatingFileHandler(
            log_file,
            maxBytes=1024 * 1024 * 10,
            backupCount=5
        )
        fh.setLevel(logging.INFO)
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

