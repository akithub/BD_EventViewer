from django.db import models

# Create your models here.

class Event(models.Model):
    PERIOD_CHOICE = (
        (1, 'Daily'),
        (2, 'Temporarily'),
        (3, 'Forever')
    )
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    content = models.TextField()
    period = models.IntegerField(choices=PERIOD_CHOICE)
    url = models.URLField()
    def __str__(self):
        return self.title
