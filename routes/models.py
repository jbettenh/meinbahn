from django.db import models


class Route(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(default=1)
    stop_id = models.CharField(max_length=8, default="20018107")
    direction = models.CharField(max_length=200, default="RBG:71707: :R")
    name = models.CharField(max_length=50, default="stop name")
    archive = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now_add=True)
    date_archived = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
