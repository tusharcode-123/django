from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import tebal
from .form import form1

# Create your views here.
def pre(request):
    return HttpResponse("hello world")

def pre2(request):
    data=tebal.objects.all()
    context={
        "data":data
    }
    return render(request,'test.html',context)

def pre3(request,id):
    data=tebal.objects.get(id=id)
    context={
        "data":data
    }
    return render(request,'test2.html',context)

def pre4(request):
    form = form1(request.POST or None)
    if form.is_valid():
	    form.save()
	    return redirect('/message/')
    context={
        "form":form
    }
    return render(request,'test3.html',context)

def pre5(request,id):
    data = tebal.objects.get(id=id)
    form = form1(request.POST or None,instance=data)
    if form.is_valid():
        form.save()
        return redirect('/message/')
    context={
        "form":form
    }
    return render(request,'test4.html',context)

def pre6(request,id):
    data = tebal.objects.get(id=id)
    data.delete()
    return redirect('/message/')
