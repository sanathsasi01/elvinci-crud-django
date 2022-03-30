from dataclasses import fields
from pyexpat import model
from django import forms
from .models import *


class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'


class StudentInstrumentsForm(forms.ModelForm):
    # student = forms.IntegerField(required=False)
    class Meta:
        model = StudentInstruments
        fields = '__all__'
