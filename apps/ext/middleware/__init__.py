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
                self.reader = geoip2.database.Reader(mmdb + "test")
            except FileNotFoundError as e:
                logger.info(e)
                self.reader = None
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

        if self.reader is not None:
            try:
                res = self.reader.country(_client_ip)
                logger.info(res.country.iso_code)
                request.iso_code = res.country.iso_code
            except AddressNotFoundError as e:
                logger.info(e)
