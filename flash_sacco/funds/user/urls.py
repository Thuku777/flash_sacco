from django.urls import path, include
from . import views
from . views import UserPage, Member,History, Loans

app_name = 'user'
urlpatterns = [
    path('', UserPage.as_view(), name='index'),
    path('members/', Member.as_view(), name='members' ),
    path('history/', History.as_view(), name='history' ),
    path('loans/', Loans.as_view(), name='loans' ),

]
