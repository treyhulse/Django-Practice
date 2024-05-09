from django import forms
from .models import GondolaShelving

class GondolaShelvingForm(forms.ModelForm):
    class Meta:
        model = GondolaShelving
        fields = '__all__'

