from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class WatchListPagination(PageNumberPagination):
    page_size = 10
    # page_query_param = 'p'  # by default, it is page
    page_size_query_param = 'page-size'
    # max_page_size = 100
    # last_page_strings = 'end'  by default, it is last


class WatchListLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    limit_query_param = 'limit'
    offset_query_param = 'start'


class WatchListCursorPagination(CursorPagination):
    page_size = 10
    ordering = 'created'
    cursor_query_param = 'record' # by default, it is cursor