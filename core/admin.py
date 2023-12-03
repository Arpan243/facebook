from django.contrib import admin
from core.models import (
    Group,
    GroupPost,
    Page,
    PagePost,
    Post,
    Friend,
    FriendRequest,
    Comment,
    Gallery,
    ReplyComment,
    Notification,
)

# Register your models here.


class GalleryAdminTab(admin.TabularInline):
    model = Gallery


class PostAdmin(admin.ModelAdmin):
    inlines = [GalleryAdminTab]
    list_editable = ["visibility"]
    list_display = ["thumbnail", "user", "title", "visibility"]
    prepopulated_fields = {"slug": ("title",)}


class GalleryAdmin(admin.ModelAdmin):
    list_editable = ["active"]
    list_display = ["thumbnail", "post", "active"]


class FriendRequestAdmin(admin.ModelAdmin):
    list_editable = ["status"]
    list_display = ["sender", "receiver", "status"]


class FriendAdmin(admin.ModelAdmin):
    list_display = ["user", "friend"]


class CommentTabAdmin(admin.TabularInline):
    model = Comment


class ReplyCommentTabAdmin(admin.TabularInline):
    model = ReplyComment


class CommentAdmin(admin.ModelAdmin):
    inlines = [ReplyCommentTabAdmin]
    list_display = ["user", "post", "comment", "active"]


class ReplyAdmin(admin.ModelAdmin):
    list_display = ["user", "comment", "active"]


class NotificationAdmin(admin.ModelAdmin):
    list_display = ["user", "notification_type", "sender", "post", "comment", "is_read"]

class GroupAdmin(admin.ModelAdmin):
    # inlines = [GroupPostTabAdmin]
    list_editable = ['user', 'name', 'visibility']
    list_display = ['thumbnail', 'user', 'name', 'visibility']
    prepopulated_fields = {"slug": ("name", )}

class PageAdmin(admin.ModelAdmin):
    # inlines = [GroupPostTabAdmin]
    list_editable = ['user', 'name', 'visibility']
    list_display = ['thumbnail', 'user', 'name', 'visibility']
    prepopulated_fields = {"slug": ("name", )}

class GroupPostTabAdmin(admin.TabularInline):
    model = GroupPost


admin.site.register(Post, PostAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Friend, FriendAdmin)
admin.site.register(FriendRequest, FriendRequestAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(ReplyComment, ReplyAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(GroupPost)
admin.site.register(PagePost)