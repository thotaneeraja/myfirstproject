from .models import next
from django import forms
class nextForm(forms.ModelForm):
       class Meta:
           model=next
           fields='__all__'