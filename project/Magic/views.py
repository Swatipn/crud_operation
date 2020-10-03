from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.conf import settings
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def handleBlog(request):
    if not request.user.is_authenticated:
        messages.error(request,'Please login and Try again!!')
        return redirect('/login')
    return render(request,'handleBlog.html')

def services(request):
    return render(request,'services.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        num = request.POST['num']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1!=pass2:
            messages.error(request,'Password not matching!!')
            return redirect('/signup')
        
        try:
            if User.objects.get(username=username):
                messages.error(request,'Username is already taken')
                return redirect('/signup')
            elif User.objects.get(email=email):
                messages.error(request,'email is already taken try with other email')
                return redirect('/signup')
           
        except Exception as identifier:
            pass    
            myuser=User.objects.create_user(username,email,pass1)
            myuser.firstname=firstname
            myuser.lastname=lastname
            myuser.num=num
            myuser.save()
            messages.success(request,'Signup successfull!!')
            return redirect('/')
    return render(request,'auth/signup.html')

      


       
    
def handlelogin(request):
    if request.method == 'POST':
        handleusername = request.POST['username']
        handlepassword = request.POST['pass1']
        user=authenticate(username=handleusername,password=handlepassword)
        if user is not None:
            login(request,user)
            messages.info(request,'Welcome to My website')
            return redirect('/')
        else:
            messages.warning(request,"Invalid credentials")
            return redirect('/login')
    return render(request,'auth/login.html')   


def handlelogout(request):
    logout(request)
    messages.success(request,'log out successful')
    return redirect('/login')
    