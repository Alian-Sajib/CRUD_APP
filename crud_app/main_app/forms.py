from django import forms
from main_app.models import stock
from bootstrap_datepicker_plus.widgets import DatePickerInput

class AddNew(forms.ModelForm):
    date = forms.DateField(widget=DatePickerInput)
    class Meta:
        model = stock
        fields = '__all__'