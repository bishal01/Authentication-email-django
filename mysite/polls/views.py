from django.shortcuts import render
from .forms import registerforms
import uuid
from django.shortcuts import redirect
from .models import customer
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required()
def home(request):
    return render(request,'home.html')
def register(request):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            forms=registerforms()
            if request.method=="POST":
                forms=registerforms(request.POST)
                if forms.is_valid():
                    user=forms.save()
                    token=str(uuid.uuid4())
                    email=user.email
                    customer.objects.create(
                        user=user,
                        name=user.username,
                        token=token,
                        email=email
                    )
                    sendmail(email,token)
                    return redirect('tokenmsg')

            
            context={
        'forms':forms
    }
        return render(request,'register.html',context)

     


def verify(request,token):
    try:
        prof_obj=customer.objects.filter(token=token).first()
        if prof_obj:
            prof_obj.is_varified=True
            prof_obj.save()
            return redirect('login')
        else:
            return redirect('error')
    except Exception as e:
        print(e)

def logins(request):
    if request.method == 'POST':
         username = request.POST.get('username')
         password = request.POST.get('password')

         user_obj = User.objects.filter(username = username).first()
         if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('login')
        
        
         profile_obj = customer.objects.filter(user = user_obj ).first()

         if not profile_obj.is_varified:
            messages.success(request, 'Profile is not verified check your mail.')
            return redirect('login')

         user = authenticate(username = username , password = password)
         if user is None:
            messages.success(request, 'Wrong password.')
            return redirect('login')
         login(request , user)
         return redirect('home') 
    return render(request,'login.html')  

def error(request):
    return HttpResponse("error")   

def logoutpage(request):
    logout(request)
    return redirect('login')




def varifiedmsg(request):
    return render(request,'varified.html')

def tokenmsg(request):
    return render(request,'tokenmsg.html')

def sendmail(email,token):
  subject = 'Your accounts need to be verified'
  message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
  email_from = settings.EMAIL_HOST_USER
  recipient_list = [email]
  send_mail(subject, message , email_from ,recipient_list )


def forget_pass(request):
    return render(request,'forget_pass.html')