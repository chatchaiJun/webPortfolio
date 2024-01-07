from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=120)
    category = models.CharField(max_length=120,blank=True)
    post = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now = True)
    featured_pic = models.ImageField(upload_to="featured_images",blank=True)
    def __str__(self) -> str:
        return self.title