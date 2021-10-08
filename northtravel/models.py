from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post_North(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    image = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
