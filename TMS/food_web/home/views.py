from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

def home_page(request):
    return render(request, "home.html")

    def contact(request):
        if request.method == "POST":
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            phone = request.POST.get('phone', '')
            desc = request.POST.get('desc', '')
            contact = Contact(name=name, email=email, phone=phone, desc=desc)
            contact.save()
        return render(request, "home/home.html")

def SignUp(request):
    if request.method == 'POST':
        username= request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.error(request, 'username taken')
                return redirect('/SignUp/')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'email taken')
                return redirect('/SignUp/')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                print('User created')
                messages.info(request, "Registered Successfully")
                return redirect('/Login/')
        else:
            messages.error(request, 'password not matching')
            return redirect('/SignUp/')
            return redirect('/')

    else:
        return render(request, 'home/SignUp.html')

def Login(request):
    if request.method == 'POST':
        login_username = request.POST['usernameL']
        login_password = request.POST['passwordL']
        user = auth.authenticate(username=login_username, password=login_password)
        if user is not None:
            auth.login(request, user)
            messages.info(request, "Successfully Logged in")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('/SignUp/')

    else:
        return render(request, 'home/SignUp.html')


def Logout(request):
    auth.logout(request)
    messages.info(request, "Successfully Logged Out")
    return redirect('/')

def profile(request):
    if request.user.is_authenticated:
        return render(request,'home/profile.html')
    else:
        return redirect('/Login/')




