from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Author, Article, ArticleCategory, Chapter


class UserSerializerNested(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "is_staff"]


class AuthorSerializer(serializers.ModelSerializer):

    # user = UserSerializerNested()

    class Meta:
        model = Author
        fields = ['user', 'age', 'created_at']


# class UserSerializer(serializers.ModelSerializer):
#     author = AuthorSerializer()

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'author']

#     def create(self, validated_data):
#         author_data = validated_data.pop('author')
#         user = User.objects.create(**validated_data)
#         Author.objects.create(user=user, **author_data)
#         return user

#     def update(self, instance, validated_data):
#         author_data = validated_data.pop('author')
#         author = instance.author

#         instance.username = validated_data.get('username', instance.username)
#         instance.email = validated_data.get('email', instance.email)
#         instance.save()


class ArticleListSerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField()
    # author = serializers.StringRelatedField()

    class Meta:
        model = Article
        exclude = ["id"]


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = "__all__"


class ArticleDetailSerializer(serializers.ModelSerializer):
    chapters = ChapterSerializer(many=True)

    class Meta:
        model = Article
        fields = "__all__"
