from rest_framework.pagination import LimitOffsetPagination

class Limit10(LimitOffsetPagination):
    default_limit = 10

