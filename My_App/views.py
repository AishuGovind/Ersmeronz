from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import tabledata

def new(request):
    wel = '<h3>Welcome to my Django Project!!</h3>'
    return HttpResponse(wel)
def index(request):
    return HttpResponse('<h1>Hi Ramya</h1>')
def first(request):
    return render(request,'first.html',{'Name': 'Aishu!'})
def myform(request):
    return render(request,'form.html')
def res(request):
    u_name = request.GET['name']
    u_age = request.GET['age']
    u_bplace = request.GET['bplace']
    return render(request, 'result.html', {'birthplace':u_bplace})
def reg(request):
    return render(request, 'register.html')
def res1(request):
    uname = request.GET['uname']
    upswd = request.GET['pswd']
    uphno = request.GET['phno']
    uemail = request.GET['email']
    return render(request,'result1.html', {'username' : uname, 'password':upswd, 'phoneno': uphno, 'email': uemail})

def style(request):
    return render (request,'styleExternal.html')

def home(request):
    newdata = tabledata.objects.all()
    if (newdata != ''):
        return render(request, 'home.html', {'ndata':newdata})
    else:
        return render(request, 'home.html')

def addData(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        contact = request.POST['contact']
        email = request.POST['email']

        obj = tabledata()
        obj.Name = name
        obj.Age = age
        obj.Contact_number = contact
        obj.Email = email
        obj.save()

        newdata = tabledata.objects.all()
        return redirect('home')
    return render(request, 'home.html')

def updateData(request):

    return render (request, 'update.html')
