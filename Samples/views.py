from django.shortcuts import render,redirect,get_object_or_404
from .models import Sample,SampleResult
from .forms import SampleForm
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError

def home(request):
    return render(request,'Samples/home.html')

def logoutuser(request):
    if request.method=='POST':
        logout(request)
        return redirect('home')
    
def loginuser(request):
    if request.method =='GET':
        return render(request,'Samples/loginuser.html',{'form':AuthenticationForm()}) 
    else:
       user = authenticate(request,username= request.POST['username'],password = request.POST['password'])
       if user is None:
           return render(request,'Samples/loginuser.html',{'form':AuthenticationForm(),'Error':'Incorrect UID or PWD'}) 
       else:
            login(request,user)
            return redirect('home')
    
def signupuser(request):
    form = UserCreationForm()
    if request.method =='GET':
        return render(request,'Samples/signupuser.html',{'form':form}) 
    else:
        #Create a new user
        if request.POST['password1']==request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('listsamples')
            except IntegrityError:
                return render(request,'Samples/signupuser.html',{'form':form,'Error':'User already Exists'}) 
        else:
            return render(request,'Samples/signupuser.html',{'form':form,'Error':'Password mismatch'}) 

def listsamples(request):
    samples = Sample.objects.filter().exclude(Status=5)
    return render(request,'Samples/listsamples.html',{'samples':samples})

def completedsamples(request):
    samples = Sample.objects.filter(Status=5)
    return render(request,'Samples/completedsamples.html',{'samples':samples})

def logsample(request):
    if request.method =='GET':
        return render(request,'Samples/logsample.html',{'form':SampleForm()})
    else:
        try: 
            form =SampleForm(request.POST)
            if form.is_valid():
                            
                newSample = form.save(commit = False)
                newSample.SampleType = form.cleaned_data['SampleType']
                newSample.Material = form.cleaned_data['Material']
                newSample.Status = form.cleaned_data['Status']

                newSample.save()
                return redirect('listsamples')
            else:
                return redirect('home')
        except :
            return render(request,'Samples/listsamples.html',{'form':form,'error':'bad data passed in'})
        

def viewsample(request,sample_pk):
    sample=get_object_or_404(Sample,pk=sample_pk)
    if request.method=='GET':
        form = SampleForm(instance=sample)
        return render(request,'Samples/sample.html',{'sample':sample,'form':form,'sampleid':sample.id})
    else:
        try:
            form =SampleForm(request.POST,instance = sample)
            form.save()
            return redirect('listsamples')
        except ValueError:
            return render(request,'Samples/sample.html',{'sample':sample,'form':form,'error':'Ding dong .... something went wrong!'})
        
def getresults(request,sample_pk):
    results = SampleResult.objects.filter(Sample=sample_pk)
    return render(request,'Samples/results.html',{'results':results})

def enterresult(request,result_pk):
    if request.method=='POST':
        result = get_object_or_404(SampleResult,pk=result_pk)#SampleResult.objects.filter(id=result_pk)
        result.Value = request.POST['value']
        result.save()
        results = SampleResult.objects.filter(Sample=result.Sample)
        return render(request,'Samples/results.html',{'results':results,'Error':'yy'})
    else:
        return render(request,'Samples/results.html',{'results':results,'Error':'yy'})


   