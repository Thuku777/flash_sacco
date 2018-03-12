from django.urls import path, include
from . import views
from .views import ConfirmRedirect, SavingsRedirect


app_name = 'transfer'
urlpatterns = [
    path('', views.formHandler, name='formHandler'),
    path('shares/', views.sharesHandler, name='sharesHandler'),
    path('success/',ConfirmRedirect.as_view() , name='confirm'),

]
