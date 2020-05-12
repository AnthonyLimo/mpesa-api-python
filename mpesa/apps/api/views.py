from django.http import HttpResponse
import requests
from requests.auth import HTTPBasicAuth
import json


def getAccessToken(request):
    consumer_key = 'VZ6fThASRSJNPwhmvFFZ4HSRuqGcNLEJ'
    consumer_secret = '8IWVfypsGpIL3KYb'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    return HttpResponse(validated_mpesa_access_token)
