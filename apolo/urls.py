from django.contrib import admin
from django.urls import path, include
from login.views import inicio_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio_view, name='inicio'),
    path('login/', include('login.urls')),
]
