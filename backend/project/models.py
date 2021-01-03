from django.db import models
class Project(models.Model):
    medium_url = models.CharField(max_length=200)
    description = models.TextField()

    ticker = models.CharField(max_length=20)
    period = models.CharField(max_length=5)
    start = models.CharField(max_length=12)
    end = models.CharField(max_length=12)
    ratio = models.CharField(max_length=20)

    def __str__(self):
        return self.ticker