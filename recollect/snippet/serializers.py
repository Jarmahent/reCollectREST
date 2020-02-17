from django.contrib.auth.models import User
from rest_framework import serializers
from snippet.models import Snippet

class SnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snippet
        fields = ("user","title", "code", "categories", "language")