
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('sysata.urls')),
    path('admin/', admin.site.urls),
]
