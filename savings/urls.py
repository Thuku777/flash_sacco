from django.urls import path, include
from . import views
from .views import  SavingsRedirect


app_name = 'savings'
urlpatterns = [
    path('',SavingsRedirect.as_view() , name='save'),

]
