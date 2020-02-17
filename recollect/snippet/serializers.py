from django.contrib.models import User
from rest_framework import serializers
from snippet.models import Snippet

class SnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "email", "date_joined")


class TodoSerializer(serializers.ModelSerializer):
    user = SnippetSerializer(read_only=True)

    class Meta:
        model = Snippet
        fields = ("user", "name", "done", "date_created")