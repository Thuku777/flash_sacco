from django.urls import path, include
from . import views
from .views import ConfirmRedirect, SavingsRedirect


app_name = 'transfer'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:username>/', views.formHandler, name='formHandler'),
    path('success/',ConfirmRedirect.as_view() , name='confirm'),

]
