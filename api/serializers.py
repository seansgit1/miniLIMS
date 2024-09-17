from rest_framework import serializers
from Samples.models import Sample

class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields =['id','Identifier','SampleType','SampleDt','Priority','Material','Status','Event','CreatedDt','UserText1']
    
    
   
   