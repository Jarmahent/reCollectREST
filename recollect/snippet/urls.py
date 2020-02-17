from django.urls import path
from snippet.views import SnippetCreateAPIView, SnippetDetailAPIView


app_name = 'snippet'

urlpatterns = [
    path('', SnippetCreateAPIView.as_view(), name="list"),
    path('<int:pk>/', SnippetDetailAPIView.as_view(), name="detail"),
]