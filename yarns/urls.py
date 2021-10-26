from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import YarnViewset, BloggerFeedView


router = DefaultRouter()
router.register(r'yarns', YarnViewset, basename='yarn')
router.register(r'feed', BloggerFeedView, basename='feed')


urlpatterns = [
    path('', include(router.urls))
]