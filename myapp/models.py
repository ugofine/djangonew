from django.db import models

# Create your models here.example we will create a blog model
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    comment = models.TextField()
    
    def __str__(self):
        return self.title 