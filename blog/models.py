from django.db import models

# from django.utils import timezone

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

    def __str__(self):
        return self.title

    def body(self):
        return self.summery[:100]

    def pub_date_pretty(self):
        if not self.pub_date:
            return "None"
        else:
            return self.pub_date.strftime('%b %e %Y')
