from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Registration


# Create your views here.
def home(request):
    return render(request, 'readmission/home.html')


def services(request):
    return render(request, 'readmission/services.html')


def appointment(request):
    return render(request, 'readmission/appointment.html')


def register(request):
    if (request.method == 'POST'):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if (password1 == password2):
            if (User.objects.filter(username=username).exists()):
                messages.warning(request, "Username already taken")
                return redirect('/register')
            elif (User.objects.filter(email=email).exists()):
                messages.warning(request, "Email already taken")
                return redirect('/register')
            elif (Registration.objects.filter(mobile=mobile).exists()):
                messages.warning(request, "Mobile number already taken")
                return redirect('/register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1,
                                                first_name=first_name, last_name=last_name)
                New_user = Registration(first_name=first_name, last_name=last_name, username=username, email=email,
                                        password=password1, mobile=mobile)
                New_user.save()
                user.save()
                messages.success(request, "Your account has been created successfully")
        else:
            messages.warning(request, "Passwords not matching")
            return redirect('/register')

        return redirect('/login')
    else:
        return render(request, "readmission/register.html")



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #    print(username)
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.warning(request, 'Invalid credentials')
            return redirect('/login')
    else:
        return render(request, "readmission/login.html")



def logout(request):
    return render(request, 'readmission/login.html')


def dashboard(request):
    return render(request, "readmission/dashboard.html")
