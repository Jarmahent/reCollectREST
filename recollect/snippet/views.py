from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from snippet.models import Snippet
from snippet.serializers import SnippetSerializer


class SnippetCreateAPIView(ListCreateAPIView):
    serializer_class = SnippetSerializer

    def get_queryset(self):
        return Snippet.objects.filter()
    
    def perform_create(self, serializer):
        serializer.save()

class SnippetDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = SnippetSerializer
