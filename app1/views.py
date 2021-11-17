from django.http import HttpResponse  #it is use for return a single html element
from django.shortcuts import render,redirect


users=[]


def homepage(request):
    #return HttpResponse('<H1>Hello Moto</H1>')
    content={ 
        'name':'chinmay',
        'pagetitle' :'cena',
        'users': users
    }
    return render(request,'index.html',content)


def page2(request):
    content={
        'pagetitle':'brock lesnar'
    }
    return render(request,'page2.html',content)

def viewform(request):
    content={
        'pagetitle':'forms'
    }
    return render(request,'form.html',content)

def +m(request):
    firstname=request.GET['firstname']
    users.append(firstname)
    return redirect('/')