from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=300)

class Project(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=300)
    github_link = models.URLField()