from django.forms import ModelForm
from .models import Sample
from StaticData.models import SampleType,Material,Status,Event
from django import forms


class SampleForm(ModelForm):

   SampleType=forms.ModelChoiceField(queryset=SampleType.objects.all())
   Material = forms.ModelChoiceField(queryset=Material.objects.all())
   Status = forms.ModelChoiceField(queryset=Status.objects.all())
   Event = forms.ModelChoiceField(queryset=Event.objects.all())

   class Meta:
        model = Sample
        fields = ['Identifier','SampleType','Material','Status','Priority','Event','UserText1']


 