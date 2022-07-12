from django.urls import path
from .views import *

app_name = "main"

urlpatterns  = [

    path('', HomePageView.as_view(), name="home"),
    path('about', AboutPageView.as_view(), name="about"),
    path('news', NewsPageView.as_view(), name="news"),
    path('contact', ContactPageView.as_view(), name="contact"),
    path('destinations', DestinationPageView.as_view(), name="destinations"),
    path('change_lang',change_lang,name="change_lang"),
    

]