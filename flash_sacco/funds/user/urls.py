from django.urls import path, include
from . import views
from . views import UserPage, Profile

app_name = 'user'
urlpatterns = [
    path('', UserPage.as_view(), name='index'),
    path('user/', Profile.as_view(), name='profile' ),
]
