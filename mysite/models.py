from django.db import models
from django.contrib.auth.models import User


class MainContent(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    main_image = models.ImageField(upload_to='content/main_images/%y/%m/%d', blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content_list = models.ForeignKey(MainContent, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='comment/images/%Y/%m/%d', blank=True)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)

    # Create your models here.

    def __str__(self):
        return f"{self.author.username} - {self.content_list.title}"
