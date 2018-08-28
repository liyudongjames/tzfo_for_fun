from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return "name: " + self.name + " age: " + str(self.age)


class Article(models.Model):
    title = models.CharField(max_length=50)
    abstract = models.TextField()
    author = models.CharField(max_length=10)
    time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __unicode__(self):
        return "title: " + self.title + " abstract: " + self.abstract + " author: " + self.author + " time: " +\
               str(self.time) + " content: " + self.content

