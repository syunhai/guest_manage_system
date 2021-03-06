from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    limit = models.IntegerField()
    status = models.BooleanField()
    address = models.CharField(max_length=150)
    start_time = models.DateField('event time')
    creat_time = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Guest(models.Model):
    event = models.ForeignKey(Event)
    realname = models.CharField(max_length=64)
    phone = models.CharField(max_length=16)
    email = models.EmailField()
    sign = models.BooleanField()
    creat_time = models.DateField(auto_now=True)

    class Meta:
        unique_together = ("event","phone")

    def __str__(self):
        return self.realname
