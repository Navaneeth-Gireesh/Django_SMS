from django.shortcuts import render, redirect
from .send_sms import send_sms
from django.contrib import messages

# Create your views here.

def sample_sms(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        number = request.POST.get('number')
        if not message or not number:
            messages.error(request, "Message and number are required.")
            return render(request, 'home.html')
        else:
            formatted_number = f'+91{number}'
            body = message
            to = formatted_number
            send_sms(body, to)
            return redirect('sms_success')
    return render(request, 'home.html')

def sms_success(request):
    return render(request, 'sms_success.html')