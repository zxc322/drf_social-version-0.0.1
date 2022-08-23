from django.db import models
from posts.models import Post
from django.conf import settings
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey

from user.models import ExtendedUser


class AbstractComment(models.Model):
    """ Abstract comment model """

    text = models.TextField(max_length=512)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text}"

    class Meta:
        abstract = True


class Comment(AbstractComment, MPTTModel):
    """ Post comment model """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE, blank=True, null=True)
    parent = TreeForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children'
    )

    def comments_count(self):
        return self.children.count()

    @property
    def likes_count(self):
        return self.comment_like.count()

    def __str__(self):
        return "{} - {}".format(self.user, self.post)



