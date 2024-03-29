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


class Cost(models.Model):
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
    payer = models.ForeignKey(User, related_name='cost_payer')
    receiver = models.ManyToManyField(
        User, related_name='cost_receiver', through='CostDetail')
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cost-detail', kwargs={'pk': self.pk})

    @staticmethod
    def get_form_fields():
        return ['name', 'amount', 'note', 'payer']


class CostDetail(models.Model):
    record = models.ForeignKey(Cost)
    user = models.ForeignKey(User)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    @staticmethod
    def get_form_fields():
        return ['user', 'amount']


class Payment(models.Model):
    group = models.ForeignKey(Group)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.CharField(max_length=200, blank=True)
    payer = models.ForeignKey(User, related_name='payment_payer')
    receiver = models.ForeignKey(User, related_name='payment_receiver')
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('payment-detail', kwargs={'pk': self.pk})

    @staticmethod
    def get_form_fields():
        return ['name', 'amount', 'note', 'payer', 'receiver']


class Balance(models.Model):
    """
    nothing here
    """
    group = models.ForeignKey(Group)
    user = models.ForeignKey(User)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.group.name + " " + self.user.username + " " \
               + str(self.balance)
