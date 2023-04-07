from django.shortcuts import redirect, render
from django.http import HttpResponse
from authentication.models import Admins
from django.contrib import messages
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

        if((len(username)==0) or (len(email)==0) or (len(password)==0) or (len(confirm_password)==0)):
            messages.info(request,"The field can not be empty")
            
        elif len(username) < 4 :
            messages.error(request,"user name length atleast 4")
            # return redirect('register')
            # return HttpResponse("user name length atleast 4")
        elif(not password == confirm_password):
            messages.error(request,"The password does not match")
            # return redirect('register')
            # return HttpResponse("The password does not match")
        
        # if not error_msg:
        else : 
            data = Admins(username=username, 
                        email=email, 
                        password=password)
            # print(data)
            data.registration()
            messages.success(request,"Register Succefully")

            # if success == True:
            #     return HttpResponse("success")
            # else:
            #     return HttpResponse("not inclueded")

    return render(request,'register.html')

def login(request):
    return render(request,'login.html')


    
