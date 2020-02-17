from django.urls import path
from snippet.views import snippets
urlpatterns = [
    path('', snippets.as_view(), name="snippets")
]