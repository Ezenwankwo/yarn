from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken

from .views import (
    BloggerCreateView, 
    ActivateAccountView,
    FollowRelationView
)

router = DefaultRouter()
router.register(r'blogger', BloggerCreateView)


urlpatterns = [
    path('', include(router.urls)),
    path('activate/<id>/<code>/', ActivateAccountView.as_view()),
    path('login/', ObtainAuthToken.as_view()),
    path('follow/<follower_id>/<following_id>/', FollowRelationView.as_view())
]