from django.db import models
from django.db.models import manager
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
# from core.title import generate_short_id
from django.urls import reverse
import random
import string

# class Password(models.Model):
#     password = models.CharField(max_length=20)
#     date = 

    # setting the passwords and the lock
    # def save(self, *args, **kwargs):
    #     if not self.passwords and self.is_locked:
    #         self.passwords = self.generate_random_passwords()
    #     super(Post, self).save(*args, **kwargs)

    # def generate_random_passwords(self, num_passwords=5, password_length=8):
    #     passwords = [''.join(random.choice(string.ascii_letters + string.digits) for _ in range(password_length)) for _ in range(num_passwords)]
    #     return ','.join(passwords)


class Phonenums(models.Model):
    name = models.CharField(max_length= 10)
    phone = models.TextField(max_length=11)
    email = models.TextField(max_length=50)
    location = models.TextField(max_length=20)
    
#Creating model manager
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Post(models.Model):
    # passwords = ForeignKey 
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length= 250)
    slug = models.SlugField(max_length=250)
    download_link = models.TextField(max_length= 1000)
    is_locked = models.BooleanField(default=True)
    author = models.CharField(max_length=10, null=True, blank=True)
    # success = models.CharField(max_length=255, editable=False, default=generate_short_id)

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    status = models.CharField(max_length=10,choices=STATUS_CHOICES, default='published')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    objects = models.Manager() #the default manager.
    published = PublishedManager() #Our custom manager.


    # For prepopulating the slug field
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('core:downloads', args=[self.slug])
