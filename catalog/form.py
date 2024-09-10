from django import forms
from django.forms import ModelForm, BooleanField
from django.core.exceptions import ValidationError

from .models import Product, Version

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = "form-check-input"
            else:
                field.widget.attrs['class'] = "form-control"

class ProductForm(StyleFormMixin, ModelForm):
    forbidden_words = [
        'казино', 'криптовалюта', 'крипта', 
        'биржа', 'дешево', 'бесплатно', 
        'обман', 'полиция', 'радар'
    ]

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['views_counter', 'created_at', 'updated_at']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        self.validate_forbidden_words(name, 'название')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        self.validate_forbidden_words(description, 'описание')
        return description

    def validate_forbidden_words(self, text, field_name):
        if text:
            for word in self.forbidden_words:
                if word in text.lower():
                    raise ValidationError(f'В {field_name} не допускаются слова: {", ".join(self.forbidden_words)}.')

class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def clean_year_born(self):
        year_born = self.cleaned_data.get('year_born')
        # Здесь можно добавить дополнительную валидацию для поля year_born, если необходимо
        return year_born