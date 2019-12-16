from django.db import models

class Blog(models.Model):

    image = models.ImageField(upload_to = 'images/blogs')
    summery = models.CharField(max_length = 200)
