from rest_framework import pagination
from rest_framework.settings import api_settings


class ExtensionPagination(pagination.PageNumberPagination):
    page_size = api_settings.PAGE_SIZE
    page_size_query_param = 'size'
    max_page_size = 1000

    def get_paginated_response(self, data):
        res = super().get_paginated_response(data)
        res.update({
            "iso_code": self.request.iso_code
        })
        return res
