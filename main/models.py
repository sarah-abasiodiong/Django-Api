from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User




class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )


    title = models.CharField(max_length=250)
    slug =   models.SlugField(max_length=250, unique_for_date='publish')
    account_emailaddress = models.EmailField(null=True)
    author = models.CharField(max_length=250, null=True)
    body =    models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,default='draft')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,default='published')


    objects = models.Manager() # The default manager.
    
    class Meta:
        ordering = ('-publish',)
        
    def __str__(self):
        return self.title


    def get_absolute_url(self):
      return reverse('main:post_detail',
                        args=[self.publish.year,
                            self.publish.month,
                            self.publish.day, 
                            self.slug]) 
                            



    