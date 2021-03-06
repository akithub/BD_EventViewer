from django.db import models
from datetime import date


class Event(models.Model):
    PERIOD_CHOICE = (
        (1, 'Daily'),
        (2, 'Temporarily'),
        (3, 'Forever'),
        (4, 'Guild'),
        (5, 'Buff'),
        (6, 'Login'),
        (7, 'Season'),
        (8, 'Perl'),
        (9, 'SNS')
    )
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    last_update = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
    overview = models.TextField(blank=True)
    content = models.TextField()
    period = models.IntegerField(choices=PERIOD_CHOICE)
    url = models.URLField(blank = True, null = True )
    def __str__(self):
        return self.title

class Info(models.Model):
    content = models.TextField(default="")
    identifier = models.CharField(max_length=200, default="")
    last_update = models.DateTimeField(auto_now=True)