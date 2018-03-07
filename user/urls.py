from django.urls import path, include
from . import views
from . views import UserPage, Member,History, Loans, Update, Register, buySharesHandler

app_name = 'user'
urlpatterns = [
    path('', UserPage.as_view(), name='index'),
    #path( 'update/<int:slug>/', prof_views.ProfileUpdate.as_view(), name='update' ),
    path('members/', Member.as_view(), name='members' ),
    path('history/', History.as_view(), name='history' ),
    path('loans/', Loans.as_view(), name='loans' ),
    path('<int:slug>/', Update.as_view(), name='profileupdate'),
    path('register/', Register.as_view(), name='register'),
    #path('shares/', BuyShares.as_view(), name='shares' ),
    path('shares/', views.buySharesHandler, name='shares' ),
]
