from django.urls import include, path
from django.contrib import admin
from rest_framework.authtoken import views


api_urls = [
    path('recollect/', include('snippet.urls')),
    path('user/', include('user.urls'))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
]