from django.contrib.auth import get_user_model

from rest_framework import serializers

from posts.models import Post, Group, Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        default=get_user_model(),
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('created', 'post',)


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Post
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'
