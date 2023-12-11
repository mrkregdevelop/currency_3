from django.urls import path, include

from account.views import ProfileView, UserSignUpView, UserActivateView

app_name = 'account'


urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('signup/', UserSignUpView.as_view(), name='signup'),
    path('activate/<uuid:username>/', UserActivateView.as_view(), name='activate'),
]
