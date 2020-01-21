from django.db import models
from django.conf import settings

class Post(models.Model):
    title   = models.CharField(max_length=100)
    content = models.TextField()
    date    = models.DateTimeField(auto_now_add=True)
    image   = models.ImageField(null=True)
    def __str__(self):
        return self.title
class Comment(models.Model):
    # When delete user, the system will delete the post
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

