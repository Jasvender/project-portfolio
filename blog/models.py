from django.db import models

# Create a Blog models
#   Title
#   public date
#   Blog Text
#   Image

# Add Blog App to settings

# Create Migration

# Migrate

# Add to admin

class Blog(models.Model):

    image   = models.ImageField(upload_to = 'images/blogs')
    date    = models.DateTimeField(default='date',null=True,blank=True)
    title   = models.CharField(max_length = 235, default='')
    summery = models.TextField()
