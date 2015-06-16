from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    members = models.ManyToManyField(User)
    time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


class Record(models.Model):
    ACTIONS = (
        ('P', 'Pay'),
        ('S', 'Split'),
    )

    project = models.ForeignKey(Project)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.CharField(max_length=200)
    payer = models.ForeignKey(User, related_name='payer')
    action = models.CharField(max_length=1, choices=ACTIONS)
    receiver = models.ForeignKey(User, related_name='receiver', blank=True)
    time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.amount)
