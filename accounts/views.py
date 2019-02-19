from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User # to check username email already exit or not
from contacts.models import Contact
# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password = request.POST['password']

        user= auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now login ')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid user')
            return redirect('login')
    else:
        return render(request,'accounts/login.html')

def register(request):
    if request.method == 'POST':
        # get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check password
        if password == password2:
          #check username
            if User.objects.filter(username=username).exists():
                messages.error(request,'That username is already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'This email is being used.')
                    return redirect('register')
                else:
                    user=User.objects.create_user(username=username,
                                                  password=password,first_name=first_name,
                                                  last_name=last_name,email=email)
                    # #login after registration
                    # auth.login(request,user)
                    # messages.success(request,'You are now login')
                    # return  redirect('index')
                    user.save()
                    messages.success(request,'You are registered and can log in')
                    return redirect('login')

        else:
            messages.error(request,'Password do not match')
            return redirect('register')

    else:
        return render(request,'accounts/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'you have logout')
        return redirect('index')


def dashboard(request):
    user_contact=Contact.objects.order_by('-contact_date').filter(user_id = request.user.id)
    context= {
        'contacts':user_contact
    }

    return render(request,'accounts/dashboard.html',context)