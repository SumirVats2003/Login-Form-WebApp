from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def login_form(request):
    return render(request, 'login_page.html')

@csrf_exempt
def submit_form(request):
    username = request.GET['username']
    password = request.GET['password']
    if username == 'sumirVats' and password == '1234':
        return render(request, 'welcome.html')
    else:
        return render(request, 'invalid.html')
