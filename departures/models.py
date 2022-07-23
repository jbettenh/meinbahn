from django.db import models

class Departure(models.Model):
    id = models.AutoField(primary_key=True)
    line = models.CharField(max_length=5, default='###')
    destination = models.CharField(max_length=50, default='')
    next_train_time = models.DateTimeField()

    def __str__(self):
        return self.destination
