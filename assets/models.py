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
    


class Project(models.Model):
    title = models.CharField(max_length=255)
    project_cover = models.ImageField(upload_to='project_pictures',blank=True)
    link_demo = models.CharField(max_length=255,blank=True)
    link_code = models.CharField(max_length=255,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Picture(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='pictures', default=1)
    image = models.ImageField(upload_to='project_pictures')
    description = models.TextField(blank=True)
    def __str__(self):
        return f"Picture {self.id} for Project {self.project.title}"
