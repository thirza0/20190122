from rest_framework import serializers
from posts import views
from .models import Post
from django.contrib.auth.models import User

class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['id', 'username']

class PostSerializer(serializers.ModelSerializer):
    likes = LikesSerializer(many = True, read_only =True)
    class Meta:
        
        model = Post
        fields = '__all__'
        read_only_fields = ['id', 'creator', 'create_at' ,'update_at']

class CommitsSerializer(serializers.ModelSerializer):
    likes = LikesSerializer(many = True, read_only =True)
    class Meta:
        
        model = Commits
        fields = '__all__'
        read_only_fields = ['id', 'creator', 'create_at' ,'update_at']


# class CreatePostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ['content']