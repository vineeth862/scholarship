from django.db import models
from django.utils import timezone

class post(models.Model):
    level = models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    method=models.CharField(max_length=100)
    title=models.CharField(max_length=1000)
    offered_by=models.CharField(max_length=1000)
    content=models.TextField()
    eligibility=models.TextField()
    Reqirements=models.TextField()
    benifits=models.TextField()
    posted_on=models.DateTimeField(default=timezone.now)
    last_date=models.DateTimeField()
    logo = models.ImageField(upload_to='logo')
    url=models.CharField(max_length=10000)



    def __str__(self):
        return self.title + '---' +self.level

class offline(models.Model):
    level = models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    method=models.CharField(max_length=100)
    title=models.CharField(max_length=1000)
    offered_by=models.CharField(max_length=1000)
    content=models.TextField()
    Reqirements=models.TextField()
    benifits=models.TextField()
    how_to_post=models.TextField()
    posted_on=models.DateTimeField(default=timezone.now)
    last_date=models.DateTimeField()
    logo = models.ImageField(upload_to='logo')
    url=models.CharField(max_length=10000)

    def __str__(self):
        return self.title + '---' + self.level