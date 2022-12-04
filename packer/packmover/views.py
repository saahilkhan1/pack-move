from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from . models import *
from datetime import date
from django.db.models import Q
# Create your views here.

def Index(request):
    return render(request,'index.html')

def EditS(request,id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    service = Services.objects.get(id=id)
    error = ""
    if request.method == 'POST':
        st = request.POST['servicetitle']
        des = request.POST['description']
        
        service.title = st
        service.description = des
        
        try:
            service.save()
            error="no"
        except:
            error = "yes"
        try:
            img = request.FILES['image']
            service.image = img
            service.save()
        except:
            pass
    return render(request,'edit_service.html',locals())

def ManageS(request):
    # if not request.user.is_authenticated:
    #     return redirect('login')
    
    service = Services.objects.all()
    return render(request,'manage_services.html',locals())

def DeleteS(request,id):
    service=Services.objects.get(id=id)
    service.delete()
    return redirect('manage_service')

def Admin_base(request):
    return render(request,'admin_base.html')

def Service(request):
    service = Services.objects.all()
    return render(request,'service.html',locals())

def Add_service(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    error = ""
    if request.method == 'POST':
        st = request.POST['servicetitle']
        img = request.FILES['image']
        des = request.POST['description']
        try:
            Services.objects.create(title=st,image=img,description=des)
            error="no"
        except:
            error="yes"
    return render(request,'add_service.html',locals())

def Login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    error=""
    if request.method == 'POST':
        u = request.POST['name']
        p = request.POST['password']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error= "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request,'login.html',locals())

def Addmin(request):
    if not request.user.is_authenticated:
        return redirect('login')
    totalservices = Services.objects.all().count()
    totalunread = Contact.objects.filter(isread="no").count()
    totalread = Contact.objects.filter(isread="yes").count()
    newbooking = SiteUser.objects.filter(status=None).count()
    oldbooking = SiteUser.objects.filter(status=1).count()
    return render(request,'addmin.html',locals())

def Logout(request):
    logout(request)
    return redirect('index')

def NewBook(request):
    if not request.user.is_authenticated:
        return redirect('login')
    booking = SiteUser.objects.filter(status=None)
    return render(request,'newbooking.html',locals())

def OldBook(request):
    if not request.user.is_authenticated:
        return redirect('login')
    booking = SiteUser.objects.filter(status=1)
    return render(request,'oldbooking.html',locals())

def About(request):
    return render(request,'about.html')

def ContactP(request):
    error = ""
    if request.method == "POST":
        name = request.POST['fullname']
        contact = request.POST['contact']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        try:
            Contact.objects.create(name=name,contact=contact,email=email,subject=subject,message=message,mdate=date.today(),isread = "no")
            error = "no"
        except:
            error = "yes"
    return render(request,'contact.html',locals())

def UserR(request):
    error = ""
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        location = request.POST['location']
        shiftingloc = request.POST['shiftingloc']
        #shiftingdate = request.POST['shiftingdate']
        requestdate = request.POST['requestdate']
        briefitem = request.POST['briefitem']
        item = request.POST['item']
        try:
            SiteUser.objects.create(name=name,email=email,mobile=mobile,location=location,
                                    shiftingloc=shiftingloc,requestdate=date.today(),briefitem=briefitem,item=item)
            error="no"
        except:
            error="yes"
    
    return render(request,'user_request.html',locals())

def View_bdetail(request,id):
    if not request.user.is_authenticated:
        return redirect('login')
    error = ""
    booking = SiteUser.objects.get(id=id)
    if request.method == 'POST':
        remark = request.POST['remark']
        try:
            booking.remark = remark
            booking.status = "1"
            booking.updationdate = date.today()
            booking.save()
            error = "no"
        except:
            error = "yes"
    return render(request,'viewbookingdetails.html',locals())

def Deloldbooking(request,id):
    booking=SiteUser.objects.get(id=id)
    booking.delete()
    return render(request,'oldbooking.html')

def UnreadQ(request):
    if not request.user.is_authenticated:
        return redirect('login')
    contact = Contact.objects.filter(isread="no")
    return render(request,'unread_quaries.html',locals())

def ReadQ(request):
    if not request.user.is_authenticated:
        return redirect('login')
    contact = Contact.objects.filter(isread="yes")
    return render(request,'read_quaries.html',locals())


def ViewQ(request,id):
    if not request.user.is_authenticated:
        return redirect('login')
    contact = Contact.objects.get(id=id)
    contact.isread="yes"
    contact.save()
    return render(request,'view_quaries.html',locals())

def Deletequarie(request,id):
    contact=Contact.objects.get(id=id)
    contact.delete()
    return render(request,'read_quaries.html')

def Search(request):
    
    if request.method == "POST":
        name = request.POST['searchdata']
        try:
            booking = SiteUser.objects.filter(Q(name=name)|Q(mobile=name))
            
        except:
            booking = ""
    return render(request,'search.html',locals())

def BookBwDate(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        fd = request.POST['fromdate']
        td = request.POST['todate']
        booking  = SiteUser.objects.filter(Q(requestdate__gte=fd) & Q(requestdate__lte=td))
        return render(request,'bookingbtdate.html',locals())
    return render(request,'bookbwdate.html',locals())

def QuariesBwDate(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        fd = request.POST['fromdate']
        td = request.POST['todate']
        contact  = Contact.objects.filter(Q(mdate__gte=fd) & Q(mdate__lte=td))
        return render(request,'quariesdate.html',locals())
    return render(request,'quariesbwdate.html',locals())

def ChangePassword(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error=""
    if request.method == "POST":
        cu = request.POST['currentpassword']
        np = request.POST['newpassword']
        try:
            u= User.objects.get(id=request.user.id)
            if u.check_password(cu):
                u.set_password(np)
                u.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"
    return render(request,'changepassword.html',locals()) 


     