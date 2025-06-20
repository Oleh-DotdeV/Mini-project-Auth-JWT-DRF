from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
  email = models.EmailField(unique=True)
  is_email_verified = models.BooleanField(default=False)


class Tag(models.Model):
  name = models.CharField(max_length=50, unique=True)

  def __str__(self):
    return self.name


class Note(models.Model):
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  title = models.CharField(max_length=255)
  content = models.TextField()
  tags = models.ManyToManyField(Tag)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title
