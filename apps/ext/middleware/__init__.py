import logging
import warnings
import geoip2.database
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from geoip2.errors import AddressNotFoundError

logger = logging.getLogger("django")

mmdb = getattr(settings, "GEOIP_PATH_MMDB", None)


class GeoIPMiddleware(MiddlewareMixin):

    def __init__(self, get_response=None):
        self.get_response = get_response
        # assert mmdb is not None
        if mmdb:
            try:
                self.reader = geoip2.database.Reader(mmdb)
            except FileNotFoundError as e:
                warnings.warn(e)
        else:
            warnings.warn("django settings GEOIP_PATH_MMDB not configured")
        self.reader = None

    def process_request(self, request):
        if "HTTP_X_FORWARDED_FOR" in request.META.keys():
            _client_ip = request.META["HTTP_X_FORWARDED_FOR"]
            logger.info(_client_ip)
        else:
            _client_ip = request.META["REMOTE_ADDR"]
            logger.info(_client_ip)

        logger.info(self.reader)
        try:
            res = self.reader.country(_client_ip)
            logger.info(res.country.name)
        except (AddressNotFoundError, AttributeError) as e:
            logger.info(e)
