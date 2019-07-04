from django import forms
from .models import Link


class UrlForm(forms.ModelForm):
    # url = forms.CharField(label='your url', max_length=2083)
    class Meta:
        model = Link
        fields = ('link_url',)


