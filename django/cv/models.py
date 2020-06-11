from django.db import models

class Bio(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='cv/img')
