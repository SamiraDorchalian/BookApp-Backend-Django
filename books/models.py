from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    language = models.CharField(max_length=100)
    link = models.URLField(max_length=500)
    cover = models.ImageField(upload_to='covers/', blank=True)
    pages = models.IntegerField()
    year = models.IntegerField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
