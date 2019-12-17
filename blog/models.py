from django.db import models

from django.utils import timezone

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
    pub_date    = models.DateTimeField(blank=True, null=True)
    title   = models.CharField(max_length = 235, default='')
    summery = models.TextField()
