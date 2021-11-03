
from django.shortcuts import render,redirect

from django.contrib import messages,auth
from django.contrib.auth.models import User

def index(request):
    return render(request, 'listings/listings.html')

def listing(request):
 if request.method =='POST':
    username = request.POST['username']
    password = request.POST['password']

    User = auth.authenticate(username = username, password = password)
   
    if User is not None:
        auth.login(request, User)
        messages.success(request, 'you are successfully logged in')
        return redirect('index')
    else:
        messages.error(request,'invalid credentials')
        return redirect('listing')
 else:
        return render(request, 'listings/listing.html')
   
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        
       
        password = request.POST['password']
        password2 = request.POST['password2']
        
          
    #check pssd
        if password == password2:
           user = User.objects.create_user(username=username, password=password2, email=email, first_name=first_name, last_name=last_name)
           user.save()
           messages.success(request, 'Successfully registered')
           return redirect('listing')

        else:
            messages.error(request, 'Passwords do not match')
           
            return redirect('register')
        
    else:
        return render(request, 'listings/register.html')

    

def logout(request):
    return redirect(request, 'index')
    
def search(request):
    return render(request, 'listings/search.html')

