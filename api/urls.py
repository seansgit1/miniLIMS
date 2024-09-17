from django.urls import path
from . import views


urlpatterns = [
    path('samples/released',views.ReleasedSampleList.as_view()),
]