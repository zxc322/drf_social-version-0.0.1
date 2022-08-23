from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Comment


@admin.register(Comment)
class CommentAdmin(MPTTModelAdmin, admin.ModelAdmin):
    """ Posts comments """

    list_display = ("user", "post", "created", "updated", "published", "id")
    mptt_level_indent = 15


# @admin.register(CommentLike)
# class CommentLikeAdmin(admin.ModelAdmin):
#     """ Comment Like """
#
#     list_display = ("id", "comment", "user")
