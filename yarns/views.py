from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ReadOnlyModelViewSet

from users.models import FollowRelation

from .serializers import YarnSerializer
from .models import Yarn


class YarnViewset(ModelViewSet):
    serializer_class = YarnSerializer
    queryset = Yarn.objects.all()
    

class BloggerFeedView(ReadOnlyModelViewSet):
    serializer_class = YarnSerializer

    def get_queryset(self):
        relations = FollowRelation.objects.filter(follower=self.request.user)
        following = [relation.following.id for relation in relations]
        yarnings = Yarn.objects.filter(blogger__in=following)
        return yarnings
