from django.db import models
from teachers.models import Teacher
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50,null=True)
    slug = models.SlugField(max_length=50,null=True,unique=True)

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=50,null=True)
    slug = models.SlugField(max_length=50,null=True,unique=True)

    def __str__(self):
        return self.name



class Course(models.Model):
    name = models.CharField(max_length=200,unique=True)
    category = models.ForeignKey(Category,null=True,on_delete=models.DO_NOTHING)
    teacher = models.ForeignKey(Teacher,blank = True,related_name='courses',on_delete = models.CASCADE)
    tags = models.ManyToManyField(Tags,blank=True)
    students = models.ManyToManyField(User,blank=True,related_name='courses')
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to = 'courses/%d/%m/%Y/',default = 'courses/default.png')
    date = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name