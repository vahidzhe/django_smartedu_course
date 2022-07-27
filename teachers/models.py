from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(default = 'teachers/%d/%m/%Y')
    facebook = models.URLField(max_length=100)
    twitter = models.URLField(max_length=100)
    linkedin = models.URLField(max_length=100)
    youtube = models.URLField(max_length=100)
    

    def __str__(self):
        return self.name