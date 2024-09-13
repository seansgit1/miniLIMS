from django.db import models

class UOM(models.Model):
    UOMName =models.CharField(max_length=100)
    CreatedDt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['UOMName']

    def __str__(self):
        return self.UOMName

class Test(models.Model):
    TestName =models.CharField(max_length=100)
    UOMID = models.ForeignKey(UOM,on_delete=models.CASCADE)
    CreatedDt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['TestName']

    def __str__(self):
        return self.TestName
    
class Event(models.Model):
    EventName =models.CharField(max_length=100)
    CreatedDt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['EventName']

    def __str__(self):
        return self.EventName
    
class Material(models.Model):
    MaterialName =models.CharField(max_length=100)
    MaterialDescription = models.CharField(max_length=150)
    CreatedDt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['MaterialName']

    def __str__(self):
        return self.MaterialName
    
class SampleType(models.Model):
    SampleTypeName =models.CharField(max_length=100)
    CreatedDt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['SampleTypeName']

    def __str__(self):
        return self.SampleTypeName
    
class Status(models.Model):
    StatusName =models.CharField(max_length=100)
    Type =models.IntegerField() 
    CreatedDt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['StatusName']

    def __str__(self):
        return self.StatusName
    
class EventTest(models.Model):
    Event =models.ForeignKey(Event,on_delete=models.CASCADE)
    Test = models.ForeignKey(Test,on_delete=models.CASCADE)
    UOM=models.ForeignKey(UOM,on_delete=models.CASCADE)
  
   


