from django import forms
from .models import Goods
import re
from django.core.exceptions import ValidationError

class GoodsForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ['title', 'description', 'is_published'] 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'rows': 5})
        self.fields['is_published'].widget = forms.CheckboxInput()
        self.fields['is_published'].widget.attrs.update({'class': 'form-check-input'})

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if re.match(r'^\d', title):
            raise ValidationError("Title can't start with a number")
        return title
