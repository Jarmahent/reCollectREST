from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from snippet.models import Snippet
from snippet.serializers import SnippetSerializer
from rest_framework import permissions

class SnippetCreateAPIView(ListCreateAPIView):
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Snippet.objects.filter()
    
    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(user=self.request.user)


class SnippetDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = SnippetSerializer
