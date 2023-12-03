from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from core.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include(("core.urls",'core'),namespace='core')),
    path("user/",include(("userauths.urls",'userauths'),namespace='userauths')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
