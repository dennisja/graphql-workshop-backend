from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.


class Link(models.Model):
    url = models.URLField()
    title = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    last_edited = models.DateTimeField(auto_now=True)
    posted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
     
