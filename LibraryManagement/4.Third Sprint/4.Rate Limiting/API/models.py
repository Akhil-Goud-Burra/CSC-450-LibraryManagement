from django.db import models

# Model 1
class Stream(models.Model):
    stream_name = models.CharField(max_length=255, verbose_name="Stream Name")

    def __str__(self):
        return self.stream_name
    

# Model 2
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title
 
    
# Model 3
class Availability(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    available_status = models.BooleanField(choices=[(True, 'Available'), (False, 'Not Available')])