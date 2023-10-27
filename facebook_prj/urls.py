from django.contrib import admin
from django.urls import path,include

from core.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include(("core.urls",'core'),namespace='core')),
    path("user/",include(("userauths.urls",'userauths'),namespace='userauths')),
]
