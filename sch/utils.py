# Helper functions
from django.contrib.gis.geoip2 import GeoIP2

from django.contrib.gis.geos import Point


def get_geo(ip):
    g = GeoIP2()
    location = Point(g.lat_lon(ip))
    return location


def get_ip_address(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print("HEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
    print(ip)
    return ip
