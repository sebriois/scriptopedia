from django import forms
from django.forms import ModelForm

from scripts.models import Script, Parameter, Option, Section

class ScriptForm(ModelForm):
    class Meta:
        model   = Script
        exclude = ('parameters',)

class ParamForm(ModelForm):
    class Meta:
        model   = Parameter
        exclude = ('options',)

class OptionForm(ModelForm):
    class Meta:
        model = Option
    
class SectionForm(ModelForm):
    class Meta:
        model = Section
    
