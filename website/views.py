from django.shortcuts import render
#from  import

def home(request):
    return render(request,'website/home.html',{})