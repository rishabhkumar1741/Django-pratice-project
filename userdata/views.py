from django.shortcuts import render,HttpResponseRedirect
from userdata.forms import signupform,loginform
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def user_login(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            form = loginform(request=request ,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,"Logged in Successfully...")
                    return HttpResponseRedirect('/')
        else:
            form = loginform()
            return render(request,'userdata/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/')




def user_signup(request):
    if request.method =='POST':
        form = signupform(request.POST)
        if form.is_valid():
            messages.success(request,"Thanks For joining us...")
            form.save()
    else:
        form = signupform()
    return render(request,'userdata/signup.html',{'form':form})




def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
