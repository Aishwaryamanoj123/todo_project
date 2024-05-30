from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from .models import *
from .forms import *





# Create your views here.
def hello(request):
    return HttpResponse("Helooooo")

# def signin(request):
#       return render(request,"signin.html")

# def signup(request):
#      return render(request, "signup.html")

def signup(request):
      if request.method == 'POST':
        username=request.POST['name']
        email=request.POST['email']
        password1=request.POST['password']
        password2=request.POST['password1']

        if password1 == password2:
               if User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Taken')
                
                return redirect('signup')
               elif User.objects.filter(email=email).exists():
                   messages.info(request,'Email Already Taken')
                   
                   return redirect('signup')
               else:
                   user=User.objects.create_user(username=username,email=email,password=password1)
                   user.save();
        else:
            messages.info(request, 'Password not matched')
            return redirect('signup')
        return redirect('signin')
      return render(request,"signup.html")



def signin(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
    
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Invalid Details')
            
            return redirect('signin')
    return render(request,"signin.html")

def home(request):
    task = Task.objects.all()
    if request.method=='POST':
        title=request.POST['title']
        date=request.POST['date']
        desc=request.POST['desc']
        status=request.POST['status']
        task = Task(title=title,description=desc,duedate=date,status=status)
        task.save()
        return redirect('home')
    return render (request,'home.html',{'tasks':task})


def delete_task(request, task_id):
    if request.method == 'POST':
       
        task = Task.objects.get(id=task_id)
        task.delete()

    return redirect('home') 


def update(request,id):
    task = Task.objects.get(id=id)
    form = tdForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request,'update.html',{'form':form , 'task':task}) 


       

                
                
               
               
             
   
          
          