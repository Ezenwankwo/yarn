from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Blogger, FollowRelation


class BloggerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=Blogger.objects.all())]
            )
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    class Meta:
        model = Blogger
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(BloggerSerializer, self).create(validated_data)


class FollowRelationSerializer(serializers.ModelSerializer):

    class Meta:
        model = FollowRelation
        fields = '__all__'