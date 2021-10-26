from rest_framework import serializers

from users.serializers import BloggerSerializer

from .models import Yarn


class RecursiveField(serializers.Serializer):
    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)
        return serializer.data


class YarnSerializer(serializers.ModelSerializer):
    blogger_info = BloggerSerializer(source='blogger', read_only=True)
    replies = RecursiveField(source='get_direct_replies', many=True, read_only=True)

    class Meta:
        model = Yarn
        fields = ['id', 'blogger', 'blogger_info', 'content', 'upload', 
                'parent_yarn', 'created', 'num_of_likes',
                'num_of_replies', 'num_of_reyarn', 'replies']
        