from django.urls import path, include
from . import views
from . views import UserPage

app_name = 'user'
urlpatterns = [
    path('', UserPage.as_view(), name='index'),

]
