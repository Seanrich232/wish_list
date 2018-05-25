from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from .models import User

def index(request):

    return render(request, "log_reg_app/index.html")
def processLogReg(request):
    result = ""
    if 'confirm' in request.POST:
        result = User.objects.validateRegistration(request.POST)
    else:
        result = User.objects.validateLogin(request.POST)
    if result['status']:
        request.session['user_id'] = result['user_id'].id
        request.session['name'] = result['user_id'].name
        return redirect('/wish')
    else:
        for error in result['errors']:
            messages.error(request, error)
    return redirect('/')
def success(request):
    return render(request, "log_reg_app/success.html")
def logout(request):
    request.session.clear()
    return redirect('/')