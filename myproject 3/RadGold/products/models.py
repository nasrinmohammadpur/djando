from django.db import models
# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
#from django import forms
from taggit.managers import TaggableManager


class Post(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'),  ('published', 'Published'), )

    tags = TaggableManager()
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='blog_posts')
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='home/%Y/%m/%d/')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES, default='draft')

    class Meta:
     ordering = ('-publish',)
    def __str__(self):
     return self.title


    def get_absolute_url(self):
        return reverse('products:post_detail', 
                        args=[self.publish.year,  self.publish.month, self.publish.day, self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Post,
                                 on_delete=models.CASCADE,
                                 related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'

#class Document(models.Model):
    #document_addr = models.ImageField(upload_to='documents/%Y/%m/%d/')
    #uploaded_at = models.DateTimeField(auto_now_add=True)        