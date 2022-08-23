from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ Posts """
    list_display = ("id", "user", "published") # , "moderation", "view_count", "id")


# @admin.register(PostLike)
# class PostLikeAdmin(admin.ModelAdmin):
#     """ Post Like """
#     list_display = ("id", "post", "user")



