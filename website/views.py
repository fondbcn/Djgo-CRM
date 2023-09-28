from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import SignupForm
from django.contrib import messages

def home(request):
    if request.method=="POST":
        user_name=request.POST["username"]
        pass_word=request.POST["password"]
        stay_logged = request.POST.get("stay_logged", "off")
        user=authenticate(request,username=user_name,password=pass_word)
        if user is not None:
            login(request,user)
            if stay_logged == "on":
                request.session.set_expiry(1209600)

            messages.success(request,"Welcome User")
            return redirect('website:home')
        else:
            messages.success(request,"Please enter valid infos!")
            return redirect('website:home')
    else:
        return render(request,'website/home.html',{})

def logout_r(request):
    logout(request)
    messages.success(request,"Trig essed")
    return redirect('website:home')
    
def signup(request):
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('website:home')
    else:
        form=SignupForm()
        return render(request,'website/signup.html',{'form':form})
    return render(request,'website/signup.html',{
       'form':form
    })