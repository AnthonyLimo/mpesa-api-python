from django.http import HttpResponse
import requests
from requests.auth import HTTPBasicAuth
import json
from . mpesa_credentials import MpesaAccessToken, LipanaMpesaPpassword
from django.views.decorators.csrf import csrf_exempt
from .models import MpesaPayment


def getAccessToken(request):
    consumer_key = 'VZ6fThASRSJNPwhmvFFZ4HSRuqGcNLEJ'
    consumer_secret = '8IWVfypsGpIL3KYb'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    # import pdb
    # pdb.set_trace()
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    return HttpResponse(validated_mpesa_access_token)


def lipa_na_mpesa_online(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
        "Password": LipanaMpesaPpassword.decode_password,
        "Timestamp": LipanaMpesaPpassword.lipa_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": 1,
        "PartyA": 254728851119,  # replace with your phone number to get stk push
        "PartyB": LipanaMpesaPpassword.Business_short_code,
        "PhoneNumber": 254728851119,  # replace with your phone number to get stk push
        "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
        "AccountReference": "Henry",
        "TransactionDesc": "Testing stk push"
    }
    response = requests.post(api_url, json=request, headers=headers)
    return HttpResponse(response.text)


def simulate(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "ShortCode": "600383",
        "CommandID": "CustomerPayBillOnline",
        "Amount": "100",
        "Msisdn": "254708374149",
        "BillRefNumber": "TestAPI"
    }
    response = requests.post(api_url, json=request, headers=headers)
    return HttpResponse(response.text)


def balance(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/accountbalance/v1/query"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "Initiator": "apitest342",
        "SecurityCredential": "OEnTXfEBwUauXnrDkVKdHP4QUJm8Q7stMX/lqsOhHC2sn+9NL7/vNaS0PBlGpbBEkmGc5XAhN+K0FLiHjYKhjOCGRKlFzuSRqyPvToSfysQUNge/rP3dinYe3IS3y7VpFWyOwSTbc0+hM+aeFB3RNM3pzMZGaYT5n5nsBNC6HsGuzryIWzoJDX2K8Qtb/xkCWfCfON0VPl6Zs+sq2nATRELK1vj6DwZ2wemDmQ2v1967MtFwu6F9spYS4IRoDo/XyYUWq+N74N7ZhvTHOhMxFww5JETfn/BPo1FuXPRXlGImi45FzFKYct7cpE2bjf9y1lPrmnv33FIf9JXoC4SAZQ==",
        "CommandID": "AccountBalance",
        "PartyA": "600744",
        "IdentifierType": "4",
        "Remarks": "Remarks",
        "QueueTimeOutURL": "http://197.248.86.122:801/timeout_url",
        "ResultURL": "http://197.248.86.122:801/result_url"
    }
    response = requests.post(api_url, json=request, headers=headers)
    return HttpResponse(response.text)


def bussiness_to_consumer(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/b2c/v1/paymentrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "InitiatorName": "apitest342",
        "SecurityCredential": "Q9KEnwDV/V1LmUrZHNunN40AwAw30jHMfpdTACiV9j+JofwZu0G5qrcPzxul+6nocE++U6ghFEL0E/5z/JNTWZ/pD9oAxCxOik/98IYPp+elSMMO/c/370Joh2XwkYCO5Za9dytVmlapmha5JzanJrqtFX8Vez5nDBC4LEjmgwa/+5MvL+WEBzjV4I6GNeP6hz23J+H43TjTTboeyg8JluL9myaGz68dWM7dCyd5/1QY0BqEiQSQF/W6UrXbOcK9Ac65V0+1+ptQJvreQznAosCjyUjACj35e890toDeq37RFeinM3++VFJqeD5bf5mx5FoJI/Ps0MlydwEeMo/InA==",
        "CommandID": "BusinessPayment",
        "Amount": "200",
        "PartyA": "601342",
        "PartyB": "254708374149",
        "Remarks": "Salary for December",
        "QueueTimeOutURL": "http://f112026d.ngrok.io/b2c_timeout_url",
        "ResultURL": "http://f112026d.ngrok.io/b2c_result_url",
        "Occasion": "DEC2019"
    }
    response = requests.post(api_url, json=request, headers=headers)
    return HttpResponse(response.text)


@csrf_exempt
def call_back(request):
    pass


@csrf_exempt
def b2c_timeout_url(request):
    context = {
        "ResultCode": 0,
        "ResultDesc": "Timed out"
    }
    return JsonResponse(dict(context))




@csrf_exempt
def b2c_result_url(request):
    context = {
        "ResultCode": 0,
        "ResultDesc": "Success"
    }
    return JsonResponse(dict(context))

def reversal(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/reversal/v1/request"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "Initiator": "apitest342",
        "SecurityCredential": "OEnTXfEBwUauXnrDkVKdHP4QUJm8Q7stMX/lqsOhHC2sn+9NL7/vNaS0PBlGpbBEkmGc5XAhN+K0FLiHjYKhjOCGRKlFzuSRqyPvToSfysQUNge/rP3dinYe3IS3y7VpFWyOwSTbc0+hM+aeFB3RNM3pzMZGaYT5n5nsBNC6HsGuzryIWzoJDX2K8Qtb/xkCWfCfON0VPl6Zs+sq2nATRELK1vj6DwZ2wemDmQ2v1967MtFwu6F9spYS4IRoDo/XyYUWq+N74N7ZhvTHOhMxFww5JETfn/BPo1FuXPRXlGImi45FzFKYct7cpE2bjf9y1lPrmnv33FIf9JXoC4SAZQ==",
        "CommandID": "TransactionReversal",
        "TransactionID": "600744",
        "Amount": "1000",
        "ReceiverParty": "600744",
        "RecieverIdentifierType": "4",
        "ResultURL": "https://197.248.86.122:801/result_url",
        "QueueTimeOutURL": "https://197.248.86.122:801/timeout_url",
        "Remarks": "Thank you",
        "Occasion": "DEC2019"
    }
    response = requests.post(api_url, json=request, headers=headers)
    return HttpResponse(response.text)


@csrf_exempt
def timeout_url(request):
    context = {
        "ResultCode": 0,
        "ResultDesc": "Timed out"
    }
    return JsonResponse(dict(context))


@csrf_exempt
def result_url(request):
    context = {
        "ResultCode": 0,
        "ResultDesc": "Success"
    }
    return JsonResponse(dict(context))

@csrf_exempt
def register_urls(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    options = {"ShortCode": LipanaMpesaPpassword.Test_c2b_shortcode,
               "ResponseType": "Completed",
               "ConfirmationURL": "https://f112026d.ngrok.io/api/v1/c2b/confirmation",
               "ValidationURL": "https://f112026d.ngrok.io/api/v1/c2b/validation"}
    response = requests.post(api_url, json=options, headers=headers)
    return HttpResponse(response.text)


@csrf_exempt
def call_back(request):
    pass


@csrf_exempt
def validation(request):
    # import pdb
    # pdb.set_trace()
    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(dict(context))


@csrf_exempt
def confirmation(request):
    mpesa_body = request.body.decode('utf-8')
    # import pdb
    # pdb.set_trace()
    mpesa_payment = json.loads(mpesa_body)
    payment = MpesaPayment(
        first_name=mpesa_payment['FirstName'],
        last_name=mpesa_payment['LastName'],
        middle_name=mpesa_payment['MiddleName'],
        description=mpesa_payment['TransID'],
        phone_number=mpesa_payment['MSISDN'],
        amount=mpesa_payment['TransAmount'],
        reference=mpesa_payment['BillRefNumber'],
        organization_balance=mpesa_payment['OrgAccountBalance'],
        type=mpesa_payment['TransactionType'],
    )
    payment.save()
    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(dict(context))
