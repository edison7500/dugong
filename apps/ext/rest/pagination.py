from rest_framework import pagination
from rest_framework.settings import api_settings


class ExtensionPagination(pagination.PageNumberPagination):
    page_size = api_settings.PAGE_SIZE
    page_size_query_param = "size"
    max_page_size = 100

    # def get_paginated_response(self, data):
    #     ret = OrderedDict(
    #         [
    #             ("next", self.get_next_link()),
    #             ("previous", self.get_previous_link()),
    #             ("results", data),
    #         ]
    #     )
    #     return Response(data=ret)
