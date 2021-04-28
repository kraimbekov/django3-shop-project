import datetime

from django.db import models

# Create your models here.



class Blog(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to='blog_img/',blank=True)
    text = models.TextField()
    create_date = models.DateField(default=datetime.datetime.now,blank=True)

    def __str__(self):
        return self.title


