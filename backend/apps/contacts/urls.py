from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.contact import ContactViewSet, LabelViewSet


router = DefaultRouter()
router.register(r'contacts', ContactViewSet, basename='contact')
router.register(r'labels', LabelViewSet, basename='label')

urlpatterns =[
    path('', include(router.urls)),
]
