from django.db import models

from django.urls import reverse

# Create your models here.
class Bloger(models.Model):
    username = models.CharField(max_length=200)
    bio = models.TextField(max_length=1000, null=True, help_text="Enter something about you")

    def get_absolute_url(self):
        return reverse('bloger-detail', args=[str(self.id)])

    def __str__(self):
        return self.username


class Blog(models.Model):
    title = models.CharField(max_length=200)
    post_date = models.DateField(null=True)
    author = models.ForeignKey('Bloger', on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1000, null=True, help_text="Описание")

    class Meta:
        ordering = ["-post_date"]

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])

    def __str__(self):
        return self.title
