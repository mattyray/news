from django.db import models


class Unit(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()  # This holds the content for each unit
    
    def __str__(self):
        return self.title
