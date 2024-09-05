from django.db import models
from StaticData.models import SampleType,Material,Status,Test,UOM

class Sample(models.Model):
    Identifier =models.CharField(max_length=100,null=True, blank=True)
    SampleType = models.ForeignKey(SampleType,on_delete=models.CASCADE,null=True, blank=True)
    SampleDt =models.DateTimeField(auto_now_add=True)
    Priority = models.BooleanField(default=False)
    Material = models.ForeignKey(Material,on_delete=models.CASCADE,null=True, blank=True)
    Status = models.ForeignKey(Status,on_delete=models.CASCADE)
    CreatedDt = models.DateTimeField(auto_now_add=True)
    UserText1 =models.CharField(max_length=100,null=True, blank=True)

    class Meta:
        ordering = ['-CreatedDt']

    def __str__(self):
        return self.Identifier

class SampleResult(models.Model):
    Sample = models.ForeignKey(Sample,on_delete=models.CASCADE)
    Test = models.ForeignKey(Test,on_delete=models.CASCADE)
    Value =models.CharField(max_length=100,null=True, blank=True)
    UOM=models.ForeignKey(UOM,on_delete=models.CASCADE)

def __str__(self):
        return self.Test

    
    

   


