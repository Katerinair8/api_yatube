from posts.models import User
from rest_framework import serializers
from posts.models import Post, Group, Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault(),
        slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all()
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('author', 'created')


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, required=False)
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    group = serializers.SlugRelatedField(
        read_only=True,
        required=False,
        slug_field='slug'
    )

    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'author', 'image', 'group', 'comments')

class GroupSerializer(serializers.ModelSerializer):
    # post = serializers.PrimaryKeyRelatedField(
    #     queryset=Post.objects.all()
    # )

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class UserSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user

    class Meta:
        model = User
        fields = "__all__"