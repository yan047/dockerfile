try:
    import urlparse
    from urllib import quote_plus
except ImportError:
    from urllib import parse as urlparse
    from urllib.parse import quote_plus
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import os
import sys
import re
import logging
from datetime import datetime
from lxml import etree
from utils import construct_url
from utils import request_xml

INV_NS = "http://www.unidata.ucar.edu/namespaces/thredds/InvCatalog/v1.0"
XLINK_NS = "http://www.w3.org/1999/xlink"
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from logging import NullHandler

_ns = {'gmd' : 'http://www.isotc211.org/2005/gmd','gco':'http://www.isotc211.org/2005/gco', 'csw':'http://www.opengis.net/cat/csw/2.0.2', 
        'wcs': 'http://www.opengis.net/wcs/2.0', 'ows':'http://www.opengis.net/ows/2.0'}

class CrawlCSW(object):

    def __init__(self, geoserver_url, logger):
        cswitems = self._crawl(url=geoserver_url, logger=logger) 
        self.datasets = cswitems

    def _crawl(self, url, logger):

        csw_url = url + "csw?service=CSW&version=2.0.2&request=GetRecords&typeNames=gmd:MD_Metadata&resultType=results&elementSetName=full&outputSchema=http://www.isotc211.org/2005/gmd&maxRecords=100"
        logger.info("\tCrawling: %s" % csw_url)
        xml_content = request_xml(csw_url, logger)
        cswitems = []
        metadatas = self._retrieveRecords(xml_content, logger) 
        wcs_refs = self._query_wcs_capabilities(url, logger)
        for rec in metadatas:
            csw = {}
            csw['id'] = self._getOneText(rec, 'gmd:fileIdentifier/gco:CharacterString')
            ident_title = self._getOneText(rec, 'gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:title/gco:CharacterString')
            root = self._improve_record( rec, ident_title, wcs_refs)
            csw['xml'] = etree.tostring( root )
            cswitems.append(csw)
        return cswitems

    def _improve_record(self, xml, ident_title, wcs_refs):
        coverageid = self._get_coverageid(ident_title, wcs_refs)
        if not coverageid:
            print ('could not find coverageid for ' + ident_title)
        else:
            wcsonline, wmsonline = self._find_wcswms(xml)
            if wcsonline is not None:
                self._improve_wcs_url(wcsonline, coverageid)
        return xml

    def _find_wcswms(self, xml):
        wcsonline = None
        wmsonline = None
        for online in xml.xpath('gmd:distributionInfo/gmd:MD_Distribution/gmd:transferOptions/gmd:MD_DigitalTransferOptions/gmd:onLine', namespaces= _ns):
            protocol = self._getOneText( online, 'gmd:CI_OnlineResource/gmd:protocol/gco:CharacterString')
            if protocol == 'OGC:WCS':
                wcsonline = online
            elif protocol == 'OGC:WMS':
                wmsonline = online
        return wcsonline, wmsonline
    

    def _improve_wcs_url(self, wcsonline, coverageid):
            url = wcsonline.xpath('gmd:CI_OnlineResource/gmd:linkage/gmd:URL', namespaces= _ns)
            if len(url) >0:
                url[0].text = url[0].text + '?SERVICE=WCS&REQUEST=GetCoverage&VERSION=2.0.1&CoverageId=' + coverageid
    
    def _get_coverageid(self, name, wcs_refs):
        for wcs in wcs_refs:
            if wcs['name'] == name:
                return wcs['coverageid'] 

    def _query_wcs_capabilities(self, url, logger):
        wcsitems = []
        wcs_url = url + 'wcs?SERVICE=WCS&REQUEST=GetCapabilities'
        logger.info("\tQuerying: %s" % wcs_url)
        wcs_content = request_xml(wcs_url, logger)
        for wcs in self._parse_wcs_refs(wcs_content, logger) :
            ref = {}
            ref['name'] = self._getOneText(wcs, 'ows:Title')
            ref['coverageid'] = self._getOneText(wcs, 'wcs:CoverageId')
            wcsitems.append(ref)
        return wcsitems

    def _parse_wcs_refs(self, wcs_content, logger):
        try:
            tree = etree.XML(wcs_content)
        except BaseException:
            logger.exception("Exception happened when paring WCS-GetCapabilities")
            return
        return 	tree.xpath('..//wcs:Contents/wcs:CoverageSummary', namespaces= _ns)

    def _getOneText(self, xml, path):
        ids = xml.xpath(path, namespaces= _ns)
        if len(ids) >0:
            return ids[0].text
        return ''

    def _retrieveRecords(self, xml_content, logger):
        try:
            tree = etree.XML(xml_content)
        except BaseException:
            logger.exception("Exception happened when paring CSW-GetRecords.")
            return
        return tree.xpath('.//gmd:MD_Metadata', namespaces= _ns)
