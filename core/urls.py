from django.urls import path

from core.views import index
app_names = "core"

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("",index, name="feed"),
]
