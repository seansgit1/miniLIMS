from django.contrib import admin
from .models import Test,UOM,Material,SampleType,Status,Event,EventTest

admin.site.register(SampleType)
admin.site.register(Material)
admin.site.register(Test)
admin.site.register(UOM)
admin.site.register(Status)
admin.site.register(Event)
admin.site.register(EventTest)




