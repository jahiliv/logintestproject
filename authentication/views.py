from django.shortcuts import render
from django.http import HttpResponse
from authentication.models import Admins
import re

def home(request):
    return HttpResponse("hi")

def signup(request):
    if request.method == 'GET':
        return render(request,'register.html')

    else:
        
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # print(username, email, password)
        confirm_password = request.POST.get('confirmpassword')

        if len(username) < 4 :
            return HttpResponse("user name length atleast 4")
        elif(not password == confirm_password):
            return HttpResponse("The password does not match")
        
        # if not error_msg:
        data = Admins(username=username, 
                        email=email, 
                        password=password)
            # print(data)
        data.registration()

            # if success == True:
            #     return HttpResponse("success")
            # else:
            #     return HttpResponse("not inclueded")

    return render(request,'register.html')

def login(request):
    return render(request,'login.html')


    
