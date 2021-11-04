from django.db import models

# Create your models here.
class events(models.Model):
    title = models.CharField(max_length=32)
    body = models.CharField(max_length=256)
    did =  models.IntegerField(blank=True, null=True)
    pid =  models.IntegerField(blank=True, null=True)
    date = models.DateField()

    def __str__(self):
      return self.title
