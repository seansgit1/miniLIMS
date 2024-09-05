from django.contrib import admin
from .models import Test,UOM,Material,SampleType,Status

admin.site.register(SampleType)
admin.site.register(Material)
admin.site.register(Test)
admin.site.register(UOM)
admin.site.register(Status)



