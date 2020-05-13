from django.urls import path
from . import views


urlpatterns = [
    path('access_token', views.getAccessToken, name='get_mpesa_access_token'),
    path('stk', views.lipa_na_mpesa_online, name='lipa_na_mpesa'),
    path('simulate', views.simulate, name='simulate'),
    path('balance', views.balance, name='balance'),

    path('b2c', views.bussiness_to_consumer, name='bussiness_to_consumer'),
    path('b2c/timeout', views.b2c_timeout_url, name="b2c_timeout_url"),
    path('b2c/result', views.b2c_result_url, name="b2c_result_url"),
    # path('b2c/callback', views.call_back, name="call_back"),


    # register, confirmation, validation and callback urls
    path('c2b/register', views.register_urls, name="register_mpesa_validation"),
    path('c2b/confirmation', views.confirmation, name="confirmation"),
    path('c2b/validation', views.validation, name="validation"),
    path('c2b/callback', views.call_back, name="call_back"),
]
