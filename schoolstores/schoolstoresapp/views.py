from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import MaterialForm


# Create your views here.
def index(request):
    return render(request, "index.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if not username or not email or not first_name or not last_name or not email or not password or not cpassword:
            messages.info(request, "The above columns are required.")
            return redirect('register')
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email,
                                                first_name=first_name,
                                                last_name=last_name)

                user.save()
                return redirect('login')
        else:
            messages.info(request, "password not matched")
            return redirect('register')

        print("user created")
        return redirect('/')
    return render(request, "register.html")

#def order(request):
   # return render(request, "order.html")

def logout(request):
    auth.logout(request)
    return redirect('/')


#def order(request):
    #message = ""
    #if request.method == 'POST':
    #    form = MaterialForm(request.POST)
     #   if form.is_valid():
     #       form.save()
     #       message = "Order placed successfully!"
      #      messages.info(request, "Order placed successfully")
  #  else:
    #    form = MaterialForm()
   # print ("Order placed successfully")
   # return render(request, 'order.html', {'form': form, 'message': message})


def order(request):
    if request.method == 'POST':
        materials = request.POST.getlist('materials')
        if materials:
            message = "Order Confirmed"
        else:
            message = "Please select at least one material before confirming the order."
        return render(request, 'order_confirmation.html', {'message': message})
    return render(request, 'order.html')
