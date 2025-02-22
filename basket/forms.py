from django import forms
from .models import ParsedData

class ParserForm(forms.Form):
    media_type = forms.ChoiceField(choices=ParsedData.MEDIA_TYPE_CHOICES, label='Media Type')
