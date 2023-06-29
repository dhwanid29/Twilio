import json
import os

from django.shortcuts import render
from twilio.rest import Client

from django.http import HttpResponse
from twilio.twiml.messaging_response import MessagingResponse
from django.http import HttpResponseRedirect, HttpResponse


def editcompany(request):
    """Edit company from admin panel"""
    a = addtaxbracket(request)
    print(a.content.decode('utf-8'), 'MM')
    return HttpResponseRedirect('/hulltecadmin/dashboard/?success=0')


# Create your views here.
def addtaxbracket(request):
    response_data = {}
    response_data['status'] = 'fail'
    response_data['message'] = 'You can not add more than 6 Tax values.'
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def send_message(request):
    account_sid = os.environ.get('ACCOUNT_SID')
    auth_token = os.environ.get('AUTH_TOKEN')
    # account_sid = 'AC8dfc5cb52d7168d8929f3bf7541eda58'
    # auth_token = '5349c87fd8de11397eb491c4c363d077'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Hello from Twilio!",
        from_='+1 534 429 0888',
        to='+918488886809'
    )

    return render(request, 'message_sent.html', {'message': message})



def twilio_webhook(request):
    message_body = request.POST.get('Body', '')
    # Process the incoming message as needed
    # Here, we're just preparing a response
    response = MessagingResponse()
    response.message(f"You said: {message_body}")
    return HttpResponse(str(response))
