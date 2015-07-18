from django import forms
from django.forms.formsets import formset_factory
from .models import *


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = Record.get_form_fields()


class CostDetailForm(forms.ModelForm):
    class Meta:
        model = CostDetail
        fields = CostDetail.get_form_fields()

CostDetailFormSet = formset_factory(CostDetailForm)
