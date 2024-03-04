from django import forms
from .models import customersDetailsModel
from .banking_choices import *


class customerDetailForm(forms.Form):
    contact = contact_category
    day = day_category
    default = default_category
    education = education_category
    housing = housing_category
    job = job_category
    loan = loan_category
    marital = marital_category
    month = month_category
    poutcome = poutcome_category

    age = forms.IntegerField()
    balance = forms.IntegerField()
    campaign = forms.IntegerField()
    contact = forms.ChoiceField(choices=contact)
    job = forms.ChoiceField(choices=job)
    day = forms.ChoiceField(choices=day)
    default = forms.ChoiceField(choices=default)
    duration = forms.IntegerField()
    housing = forms.ChoiceField(choices=housing)
    loan = forms.ChoiceField(choices=loan)
    marital = forms.ChoiceField(choices=marital)
    education = forms.ChoiceField(choices=education)
    month = forms.ChoiceField(choices=month)
    pdays = forms.IntegerField()
    poutcome = forms.ChoiceField(choices=poutcome)
    previous = forms.IntegerField()

    # class Meta:
    #     model = customersDetailsModel
    #     fields = '__all__'
