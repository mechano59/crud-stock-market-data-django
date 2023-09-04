from django import forms
from .models import JSONData

class JSONDataForm(forms.ModelForm):
    class Meta:
        model = JSONData
        fields = '__all__'  # You can adjust this to include specific fields if needed
