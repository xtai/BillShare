from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    members = models.ManyToManyField(User)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('gates:index')

    @staticmethod
    def get_form_fields():
        return ['name', 'desc']


class Record(models.Model):
    """
    (payer is not receiver, amount is negative) -->
        Payer pay back to receiver.
    (payer is not receiver, amount is positive) -->
        Receiver need to pay back to payer.
    (payer is receiver, amount has to be positive) -->
        Payer pay for the project, spilting with entire project.
    """
    group = models.ForeignKey(Group)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.CharField(max_length=200, blank=True)
    payer = models.ForeignKey(User, related_name='payer')
    receiver = models.ForeignKey(User, related_name='receiver')
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('record-detail', kwargs={'pk': self.pk})

    @staticmethod
    def get_form_fields():
        return ['name', 'amount', 'note', 'payer', 'receiver']

