from rest_framework import generics, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from ..models import Contact, Label
from ..serializers.contact import (
    ContactListSerializer,
    ContactDetailSerializer,
    LabelSerializer,
)


class DefaultPagination(LimitOffsetPagination):
    """
    - `limit`: 한 번에 가져올 데이터 개수
    - `offset`: 데이터를 가져올 시작 위치
    예: /api/contacts/?limit=10&offset=20  (21번째부터 10개 가져오기)
    """
    default_limit = 10  # 기본적으로 10개씩
    max_limit = 50      # 최대 50개까지 요청 가능


class ContactViewSet(viewsets.ModelViewSet):
    """
    Contact ViewSet.
    """
    queryset = Contact.objects.prefetch_related('labels').all()
    pagination_class = DefaultPagination
    
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['name', 'email', 'phone_number']
    ordering = ['created_at']

    def get_serializer_class(self):
        if self.action == 'list':
            return ContactListSerializer
        return ContactDetailSerializer
    

class LabelViewSet(viewsets.ModelViewSet):
    """
    Label ViewSet.
    """
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    pagination_class = DefaultPagination