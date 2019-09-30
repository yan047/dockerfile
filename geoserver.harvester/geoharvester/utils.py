import os

import requests

try:
    import urlparse
except ImportError:
    from urllib import parse as urlparse


def construct_url(url, href):
    u = urlparse.urlsplit(url)
    base_url = u.scheme + "://" + u.netloc
    relative_path = urlparse.urljoin(base_url, os.path.split(u.path)[0])

    if not href:
        return url

    if href[0] == "/":
        # Absolute paths
        cat = urlparse.urljoin(base_url, href)
    elif href[0:4] == "http":
        # Full HTTP links
        cat = href
    else:
        # Relative paths.
        cat = relative_path + "/" + href

    return cat

def request_xml(url, logger, auth=None):
    '''
    Returns an etree.XMLRoot object loaded from the url
    :param str url: URL for the resource to load as an XML
    '''
    try:
        r = requests.get(url, auth=auth, verify=False)
        return r.text.encode('utf-8')
    except BaseException:
        logger.error("Skipping %s (error parsing the XML)" % url)
    return