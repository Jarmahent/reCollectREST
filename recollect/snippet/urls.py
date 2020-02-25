from django.urls import path,include
from snippet.views import SnippetCreateAPIView, SnippetDetailAPIView


app_name = 'snippet'

urlpatterns = [
    path('', SnippetCreateAPIView.as_view(), name="list"),
    path('auth/', include('rest_auth.urls')),
    path('<int:pk>/', SnippetDetailAPIView.as_view(), name="detail")
]