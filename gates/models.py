from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    members = models.ManyToManyField(User)
    creation_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Record(models.Model):
    ACTIONS = (
        ('F', 'Pay for'),
        ('T', 'Pay to'),
        ('S', 'Split'),
    )
    group = models.ForeignKey(Group)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.CharField(max_length=200)
    payer = models.ForeignKey(User, related_name='payer')
    action = models.CharField(max_length=1, choices=ACTIONS)
    receiver = models.ForeignKey(User, related_name='receiver', blank=True)
    record_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
