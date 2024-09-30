from django import forms
from AluminumCalcApp.models import UserTolerances12_2Model

class ToleranceForms(forms.ModelForm):
    class Meta:
        model = UserTolerances12_2Model
        fields = "__all__"