from django.db import models

# Model 1
class Stream(models.Model):
    stream_name = models.CharField(max_length=255, verbose_name="Stream Name")

    def __str__(self):
        return self.stream_name