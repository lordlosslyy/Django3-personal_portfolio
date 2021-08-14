from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100) 
    text = models.TextField()

    # let admin show the title 
    def __str__(self): 
        return self.title