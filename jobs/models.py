from django.db import models

class Jobs(models.Model):
    # upload_to=None, height_field=None, width_field=None, max_length=100, **options
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
