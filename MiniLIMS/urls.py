from django.contrib import admin
from django.urls import path
from Samples import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('listsamples', views.listsamples, name='listsamples'),
    path('completedsamples', views.completedsamples, name='completedsamples'),
    path('logsample', views.logsample, name='logsample'),
    path('logoutuser', views.logoutuser , name='logoutuser'),
    path('loginuser', views.loginuser , name='loginuser'),
    path('signupuser', views.signupuser , name='signupuser'),
    path('viewsample/<int:sample_pk>', views.viewsample , name='viewsample'),
    path('getresults/<int:sample_pk>', views.getresults,name='getresults'),
    path('enterresult/<int:result_pk>/5', views.enterresult,name='enterresult'),
]
