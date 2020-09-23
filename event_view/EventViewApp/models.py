from django.db import models

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    content = models.TextField()
    period = models.IntegerField()
    url = models.URLField()
    def __str__(self):
        return self.title
