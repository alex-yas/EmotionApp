from django.forms import ModelForm, FileInput
from .models import InputAnt


class InputForm(ModelForm):
    class Meta:
        model = InputAnt
        fields = '__all__'
        widgets = {
            "image": FileInput(attrs={'class': "form-control", 'type': "file", 'accept': "image/*", 'class': "mrg", 'style': 'font-size: xx-large'})
        }
