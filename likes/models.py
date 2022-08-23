from django.db import models
from django.conf import settings

from posts.models import Post
from comments.models import Comment


class PostLike(models.Model):
    """ Post like """

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_like')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_post_like')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return 'post:{}, user:{}'.format(self.post, self.user)


class CommentLike(models.Model):
    """ Post like """

    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment_like')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_comment_like')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return 'comment:{}, user:{}'.format(self.comment, self.user)
