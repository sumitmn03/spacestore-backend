from rest_framework import (
    pagination,
    response
)


class HomepagePagination(pagination.PageNumberPagination):
    page_size = 4
    page_size_query_param = 'size'
    max_page_size = 15

    def get_paginated_response(self, data):
        context = {
            'next': self.get_next_link(),
            'results': data
        }

        return response.Response(context)
