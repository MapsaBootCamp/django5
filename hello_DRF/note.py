from django.conf import settings
import django
from rest_framework import serializers
from datetime import datetime
django.setup()


settings.configure()


class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()


comment = Comment(email='leila@example.com', content='foo bar')

`


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
    name = serializers.CharField(max_length=255, allow_null=True)

    def create(self, validated_date):
        return Comment(**validated_date)

    def update(self, instance, validated_data):
        pass


# CommentSerializer({json}) ----> create
# CommentSerializer({json}, obj) ---> update


serializer = CommentSerializer(comment)
print(serializer.data)
