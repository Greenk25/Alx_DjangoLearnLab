from django.urls import path
from .views import RegisterView, ProfileView
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
urlpatterns = [
    path('api/accounts/', include('accounts.urls')),
]
