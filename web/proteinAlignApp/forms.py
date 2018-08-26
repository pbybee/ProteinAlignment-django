from django import forms
from django.core.exceptions import ValidationError
from .models import Align
from .validators import validateAminos
import re



class PostForm(forms.ModelForm):

    reference = forms.CharField(widget=forms.Textarea,validators=[validateAminos])
    align = forms.CharField(widget=forms.Textarea,validators=[validateAminos])

    class Meta:
        model = Align
        fields = ('align','reference')

    def clean(self):
        for field in self.cleaned_data:
            self.cleaned_data[field] = re.sub(r"\W", "", self.cleaned_data[field])
        return self.cleaned_data



    # def clean_reference(self):
    #     data = self.cleaned_data['reference']
    #     re.sub(r"\W", "", data)
    #     return data
    #
    #
    # def clean_align(self):
    #     data = self.cleaned_data['align']
    #     re.sub(r"\W", "", data)
    #     return data