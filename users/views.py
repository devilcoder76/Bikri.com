from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import userdata
# Create your views here.

def reg_form(request):
    if request.session.has_key('id'):
        return HttpResponse('Logout first:')
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        user_type=request.POST.get('choice')
        data=userdata(fname=fname,lname=lname,username=username,password=password,email=email,user_type=user_type)
        data.save()
        return redirect('users:login_User')
    return render(request,"users/userform.html")

def login(request):
    if request.session.has_key('id'):
        return HttpResponse('Already logged in:')
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            data=userdata.objects.get(username=username,password=password)
        except userdata.DoesNotExist:   
            return redirect('users:userform')
        request.session['id']=data.id
        request.session['username']=data.username
        request.session['type']=data.user_type
        return redirect('products:view_product')
    return render(request,"users/login.html")

def logout(request):
    if request.session.has_key('id'):
        del request.session['id']
        del request.session['username']
    return redirect('products:view_product')
