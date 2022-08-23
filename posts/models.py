from django.db import models
from django.conf import settings
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey

from user.models import ExtendedUser


class Post(models.Model):
    """ Users post """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    text = models.TextField(max_length=1024)
    image = models.ImageField(upload_to='post/img/', blank=True, null=True)
    published = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    view_count = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return 'post #{}, author_id: {}'.format(self.id, self.user)

    def comments_count(self):
        return self.comments.filter(parent=None).count()

    def likes_count(self):
        return self.post_like.count()



