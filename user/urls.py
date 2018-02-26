from django.urls import path, include
from . import views as prof_views
from . views import UserPage, Member,History, Loans, Update, Register

app_name = 'user'
urlpatterns = [
    path('', UserPage.as_view(), name='index'),
    #path( 'update/<int:slug>/', prof_views.ProfileUpdate.as_view(), name='update' ),
    path('members/', Member.as_view(), name='members' ),
    path('history/', History.as_view(), name='history' ),
    path('loans/', Loans.as_view(), name='loans' ),
    path('<int:slug>/', prof_views.Update.as_view(), name='profileupdate'),
    path('register/', Register.as_view(), name='register'),

]
