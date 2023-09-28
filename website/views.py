from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate,get_user_model
from django.contrib import messages
from .forms import SignupForm
from .token import acc_activ_token
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage

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
            user=form.save(commit=False)
            user.is_active=False
            user.save()
            activation(request, user, form.cleaned_data.get('email'))
            return redirect('website:home')
    else:
        form=SignupForm()
        return render(request,'website/signup.html',{'form':form})
    return render(request,'website/signup.html',{
       'form':form
    })

def activation(request,user,to_email):
    mail_subject = "Activate your user account."
    message = render_to_string("website/activation.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': acc_activ_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, 'Please check you inbox to activate email!')
    else:
        messages.error(request, 'Problem sending email verification, check if you typed it correctly.')
        
def activate(request,uidb64,token):
    User=get_user_model()
    try:
        uid=force_str(urlsafe_base64_decode(uidb64))
        user=User.objects.get(pk=uid)
    except:
        user=None
    if user is not None and acc_activ_token.check_token(user,token):
        user.is_active=True
        user.save()
        messages.success(request,"Account activated")
        return redirect('website:home')
    else:
        messages.success(request,'Invalid activation')
    return redirect('website:home')