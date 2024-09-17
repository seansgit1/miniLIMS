from django.contrib import admin
from django.urls import path,include
from Samples import views

urlpatterns = [

    #Auth
    path('logoutuser', views.logoutuser , name='logoutuser'),
    path('loginuser', views.loginuser , name='loginuser'),
    path('signupuser', views.signupuser , name='signupuser'),

    #MiniLIMS
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('listsamples', views.listsamples, name='listsamples'),
    path('releasedsamples', views.releasedsamples, name='releasedsamples'),
    path('logsample', views.logsample, name='logsample'),
    path('viewsample/<int:sample_pk>', views.viewsample , name='viewsample'),
    path('getresults/<int:sample_pk>', views.getresults,name='getresults'),
    path('enterresult/<int:result_pk>', views.enterresult,name='enterresult'),

    #API
    path('api/', include('api.urls')),
]
