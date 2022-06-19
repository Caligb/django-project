from cgitb import text
from multiprocessing import AuthenticationError
from turtle import title
from typing import Text
from django.db import models
from django.forms import SlugField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey()
    created_date = models.DateTimeField()
    published_date = models.DateTimeField()
