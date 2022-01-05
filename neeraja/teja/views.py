from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import next
from.forms import nextForm
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required,permission_required

def func(request):
    return HttpResponse("neeraja")

def cre(request):
    return HttpResponse("obulamma")
@login_required()
def index(request):
    data = next.objects.all()
    dict = {'studata': data}
    return render(request, 'index.html', dict)
@login_required()
def create(request):
    if request.method=='POST':

        form=nextForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/index/')
    else:
            form=nextForm()
    return render(request,'create.html',{'form':form})
@login_required()
def edit(request,name):
     studata=next.objects.get(name=name)
     form=nextForm(instance=studata)
     return render(request,'update.html',{'form':form,'name':name})
@login_required()
def delete(request,name):
    studata=next.objects.get(name=name)
    studata.delete()
    return redirect('/index/')
@login_required()
def update(request,name):
    studata=func.objects.get(name=name)
    form=nextForm(request.POST,instance=studata)
    if form.is_valid():
        form.save()
        return redirect('/index/')
    return render(request,'update.html',{'form':form,'name':name})

def home(request):
    return render(request,'home.html')
# @login_required()
def user_logout(request):
    return render(request,'logout.html')


# Create your views here.
