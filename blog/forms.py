# blog/forms.py

from django import forms
from .data import AVAILABLE_THEMES, AVAILABLE_LANGUAGES

class PreferencesForm(forms.Form):
    theme = forms.ChoiceField(
        choices=AVAILABLE_THEMES.items(),
        label="Тема оформления",
        required=False # Делаем необязательным, чтобы можно было не менять
    )
    language = forms.ChoiceField(
        choices=AVAILABLE_LANGUAGES.items(),
        label="Язык интерфейса",
        required=False
    )