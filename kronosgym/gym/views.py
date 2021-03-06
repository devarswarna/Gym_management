from gym.models import Enquiry
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout,login

from .models import *



# Create your views here.
def About(request):
    return render(request,'about.html')


def Contact(request):
    return render(request,'contact.html')


def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    enquiry=Enquiry.objects.all()
    e1=0
    for i in enquiry:
        e1+=1
    d={'e1':e1}
    return render(request,'index.html',d)


def Login(request):
    error=""
    if request.method=='POST':
        u=request.POST["uname"]
        p=request.POST["pwd"]
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request, user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'login.html', d)


def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

def Add_enq(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=="POST":
        n=request.POST['name']
        c=request.POST['contact']
        e=request.POST['emailid']
        a=request.POST['age']
        g = request.POST['gender']
        try:
            Enquiry.objects.create(name=n,contact=c,email=e,age=a,gender=g)
            error="no"
        except:
            error="yes"
    d ={'error':error}
    return render(request,'add_enquiry.html', d)


def View_enq(request):
    if not request.user.is_staff:
        return redirect('login')
    enq = Enquiry.objects.all()
    d = {'enq':enq}
    return render(request,'view_enquiry.html', d)



def Delete_enq(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    enquiry=Enquiry.objects.get(id=pid)
    enquiry.delete()
    return render('view_enquiry')



def Add_Equipment(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=="POST":
        n=request.POST['name']
        p=request.POST['price']
        u=request.POST['unit']
        d=request.POST['date']
        de=request.POST['description']
        try:
            Equipment.objects.create(name=n,price=p,unit=u,date=d,description=de)
            error="no"
        except:
            error="yes"
    d ={'error':error}
    return render(request,'add_equipment.html', d)



def View_Equipment(request):
    if not request.user.is_staff:
        return redirect('login')
    equipment=Equipment.objects.all()
    d = {'equipment':equipment}
    return render(request,'view_equipment.html', d)


def Delete_Equipment(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    equipment=Equipment.objects.get(id=pid)
    equipment.delete()
    return render('view_equipment')




def Add_Plan(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=="POST":
        n=request.POST['name']
        a=request.POST['amount']
        du=request.POST['duration']
        try:
            Plan.objects.create(name=n,amount=a,duration=du)
            error="no"
        except:
            error="yes"
    d ={'error':error}
    return render(request,'add_plan.html', d)



def View_Plan(request):
    if not request.user.is_staff:
        return redirect('login')
    plan=Plan.objects.all()
    d = {'plan':plan}
    return render(request,'view_plan.html', d)


def Delete_Plan(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    plan=Plan.objects.get(id=pid)
    plan.delete()
    return render('view_plan')



def Add_Member(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    plan1= Plan.objects.all()
    if request.method=="POST":
        n=request.POST['name']
        c = request.POST['contact']
        e=request.POST['email']
        a=request.POST['age']
        g = request.POST['gender']
        p=request.POST['plan']
        j=request.POST['joindate']
        ex=request.POST['expiredate']
        i=request.POST['initalamount']
        plans=Plan.objects.filter(name=p).first()
        try:
            Member.objects.create(name=n,contact=c,email=e,age=a,
            gender=g,plan=plans,joindate=j,expiredate=ex,initalamount=i)
            error="no"
        except:
            error="yes"
    d ={'error':error,'plan':plan1}
    return render(request,'add_member.html', d)



def View_Member(request):
    if not request.user.is_staff:
        return redirect('login')
    member=Member.objects.all()
    d = {'member':member}
    return render(request,'view_member.html', d)


def Delete_Member(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    member=Member.objects.get(id=pid)
    member.delete()
    return render('view_Member')
