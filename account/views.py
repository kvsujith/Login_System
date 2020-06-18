from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


from django.contrib.auth.models import auth,User


# Create your views here.


def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print('logged')

            return redirect('/')

        else:
            messages.info(request, 'Invalid credentials')
            print('Invalid credentials')
            return render(request, 'Admin_Login.html')

    return render(request,'UserLogin.html')

@login_required(login_url="/login")
def home(request):
    # This code request.user.is_superuser is checks whether admin is logged in or normal user is logged in
    if  request.user.is_superuser:
        return redirect('/register')

    return render(request,'UserProfile.html')


def logout(request):
    if  request.user.is_superuser:
        auth.logout(request)
        return render(request, 'Admin_Login.html')
    auth.logout(request)
    return render(request,'UserLogin.html')

@login_required(login_url='/')
def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['pswd1']
        password2 = request.POST['pswd2']

        if password1 == password2:

            if User.objects.filter(username=username).exists():
                messages.info(request, 'Email is Already taken')
                return redirect('/register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.info(request, 'Email id is Already Exists')
                    return redirect('/register')
                else:
                    user = User.objects.create_user(username=username, first_name=fname, last_name=lname, email=email,
                                                    password=password1)
                    user.save()
                    print('user created')
                    messages.info(request, 'Viwers created Successfully')
                    return HttpResponseRedirect('/register')
        else:
            messages.info(request, 'Password Miss match')
            return redirect('/register')
    else:
        return render(request, 'register.html')
