from django import forms
from .models import Page, Section, Element, Theme
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'jscript']

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['name']

class ElementForm(forms.ModelForm):
    class Meta:
        model = Element
        fields = ['element_type', 'content', ]
        widgets = {
            'element_type': forms.RadioSelect,  # Use radio buttons for element_type
        }

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class HTMLImportForm(forms.Form):
    title = forms.CharField()
    strip = forms.BooleanField(required=False, initial=True, label='Strip JavaScript')
    html_file = forms.FileField(label='Upload HTML File')

class PageContentForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': 20,  # Adjust the height of the textarea
                'cols': 80,  # Adjust the width of the textarea
                'style': 'width: 90%; height: 500px; resize: vertical;',  # Make it scrollable and resizable
            }
        ),
        label='HTML', required = False
    )

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, label="Search")

class ThemeSelectForm(forms.Form):
    theme = forms.ModelChoiceField(queryset=Theme.objects.all(), empty_label="Select a Theme")

