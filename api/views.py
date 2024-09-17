from rest_framework import generics,permissions
from . import views
from .serializers import SampleSerializer
from Samples.models import Sample

class ReleasedSampleList(generics.ListAPIView):
   serializer_class =  SampleSerializer
   permission_class = [permissions.IsAuthenticated]

   def get_queryset(self):
      return Sample.objects.filter(Status=5).order_by('-id')

