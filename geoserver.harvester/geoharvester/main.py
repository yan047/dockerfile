from harvest import GeoServerHarvester
from crawlcsw import CrawlCSW
import sys

def usage():
    """Provide usage instructions"""
    return '''
python main.py http://localhost/geoserver/ /home/user
'''

print ('argument number =' + str(len(sys.argv)))

for arg in sys.argv:
    print(arg)
if len(sys.argv) < 3:
    print(usage())
    sys.exit(1)

GeoServerHarvester(geoserver_url=sys.argv[1] ,
                    out_dir=sys.argv[2])