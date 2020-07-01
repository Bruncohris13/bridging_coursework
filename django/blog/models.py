from django.conf import settings
from django.db import models
from django.utils import timezone
from markdownx.utils import markdownify


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(default="<p class='post-text'> </p>")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def formatted_markdown(self):
        return markdownify(self.text)

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.author +" in " + str(self.post)