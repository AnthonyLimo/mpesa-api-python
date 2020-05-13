from django.urls import path
from . import views


urlpatterns = [
    path('access_token', views.getAccessToken, name='get_mpesa_access_token'),
    path('stk', views.lipa_na_mpesa_online, name='lipa_na_mpesa'),
    path('simulate', views.simulate, name='simulate'),

    path('balance', views.balance, name='balance'),
    path('balance/timeout', views.timeout_url, name="timeout_url"),
    path('balance/result', views.result_url, name="result_url"),
    path('balance/callback', views.call_back, name="call_back"),


    path('b2c', views.bussiness_to_consumer, name='bussiness_to_consumer'),
    path('b2c/timeout', views.timeout_url, name="timeout_url"),
    path('b2c/result', views.result_url, name="result_url"),
    path('b2c/callback', views.call_back, name="call_back"),


    # register, confirmation, validation and callback urls
    path('c2b/register', views.register_urls, name="register_mpesa_validation"),
    path('c2b/confirmation', views.confirmation, name="confirmation"),
    path('c2b/validation', views.validation, name="validation"),
    path('c2b/callback', views.call_back, name="call_back"),
]
