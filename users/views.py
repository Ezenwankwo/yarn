import pyotp
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from .serializers import BloggerSerializer
from .models import Blogger, FollowRelation


class BloggerCreateView(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = BloggerSerializer
    queryset = Blogger.objects.all()


class ActivateAccountView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, id, code):
        blogger = get_object_or_404(Blogger, pk=id)
        blogger_id = blogger.id
        hotp = pyotp.HOTP('base32secret3232')
        if hotp.verify(code, blogger_id):
            blogger.is_active = True
            blogger.save()
            return Response({'message': 'Account Activated'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid Token'}, status=status.HTTP_406_NOT_ACCEPTABLE)


class FollowRelationView(APIView):
    """
    Bloggers can follow and unfollow each other
    """
    permission_classes = [AllowAny]
    
    def get(self, request, follower_id, following_id):
        follower = get_object_or_404(Blogger, pk=follower_id)
        following = get_object_or_404(Blogger, pk=following_id)
        relation = FollowRelation.objects.filter(follower=follower, following=following)
        if relation.exists():
            relation.delete()
            return Response({'message': 'unfollowed'}, status=status.HTTP_200_OK)
        else:
            FollowRelation.objects.create(follower=follower, following=following)
        return Response({'message': 'followed'}, status=status.HTTP_201_CREATED)
