from django.urls import path
from . import views


urlpatterns = [
    path('access_token', views.getAccessToken, name='get_mpesa_access_token'),
    path('stk', views.lipa_na_mpesa_online, name='lipa_na_mpesa'),
]
