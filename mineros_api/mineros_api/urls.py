from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),
    path('', include('core.urls')),
    path('api/authentication/', include('dj_rest_auth.urls')),
    path('api/registration/', include('dj_rest_auth.registration.urls')),
    
]