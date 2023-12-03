from django.urls import path

from core import views
app_names = "core"

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("",views.index, name="feed"),

    # Ajax path
    path("create-post/", views.create_post, name="create-post"),
    path("like-post/", views.like_post, name="like-post"),
]
