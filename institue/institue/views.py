from django.http import HttpResponse 
from django.urls import reverse

from database.models import Homepagepicture, Gallerypicture, Subject,Notes, Teacherpicture,Student, Contact, Testinomial, Notice, Topbackpage, Tophomepage,CustomUser,profile
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from database.email import EmailBackend
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .helper import sent_forget_password_mail
import uuid

def index(request):

    notice = Notice.objects.all().order_by('-id')[:5] 
    homepicture = Homepagepicture.objects.all().order_by('-id')[:5] 
    tophomepage = Tophomepage.objects.all().order_by('-id')[:3] 
    testinomial = Testinomial.objects.all().order_by('-id')[:3] 

    gallery = Gallerypicture.objects.all().order_by('-id')[:3]
    gallery1 = Gallerypicture.objects.all().order_by('-id')[3:6]
    gallery2 = Gallerypicture.objects.all().order_by('-id')[6:7]
    
    data = {
        
        'notice': notice,
        'homepicture' : homepicture,
        'tophomepage' : tophomepage,
        'gallery': gallery,
        'gallery1': gallery1,
        'gallery2':gallery2,
        'testinomial':testinomial
        
    }
    return render (request, "index.html",data)

def about(request):
    return render (request, "aboutus.html")

def event(request):
    gallery = Gallerypicture.objects.all().order_by('-id')[:2]
    data = {
        'gallery': gallery,
        
        
    }
    return render (request, "event.html",data)

def teacher(request):
    return render (request, "teacher.html")
def search(request):
    if request.method == "POST":
        userid = request.POST.get('userid')
        user = Subject.objects.filter(userid=userid).all
        student = Student.objects.filter(userid = userid).first()
        data = {
            'user':user,
            'student':student
        }
        return render (request, "resultdetails.html",data)
def notes(request):
    class6 = Notes.objects.filter(study = '6').all
    class7 = Notes.objects.filter(study = '7').all
    class8 = Notes.objects.filter(study = '8').all
    class9 = Notes.objects.filter(study = '9').all
    class10 = Notes.objects.filter(study = '10').all
    class11 = Notes.objects.filter(study = '11').all
    class12 = Notes.objects.filter(study = '12').all

    data = {
        'class6' : class6,
        'class7' : class7,
        'class8' : class8,
        'class9' : class9,
        'class10' : class10,
        'class11': class11,
        'class12' : class12
        
    }
    
        
    return render (request, "notes.html",data)

    
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email') or None
        msg = request.POST.get('msg')

        contact = Contact(
            name = name,
            phone = phone,
            email = email,
            msg = msg,


        )
        contact.save()
        messages.success(request , 'Message is Sent')
        return redirect('home')

    return redirect('home')

def course(request):
    return render (request, "course.html")

def foundation(request):
    return render (request, "foundationcourse.html")
def eleven(request):
    return render (request, "1112th.html")
def jeedetails(request):
    return render (request, "jeecourse.html")
def neetdetails(request):
    return render (request, "neetcourse.html")
def topper(request):
    return render (request, "topper.html")

def result(request):
    return render (request, "result.html")


def verifyuserid(request):
    if request.method == "POST":
        userid = request.POST.get('userid')
        if not CustomUser.objects.filter(userid = userid).first():
            messages.success(request, "No User is found Please check Your User id")
            return render (request, "dashboard\\forget1.html")
        else :

            user = CustomUser.objects.filter(userid = userid).first()
            usermail = user.email
            token = str(uuid.uuid4())

            profile_obj = profile.objects.create(userid = user, forget_token = token)
            sent_forget_password_mail(usermail , token)
            print(token)

            
            messages.success(request, "An Email is sent to your email address")
            return render (request, "dashboard\\forget1.html")
        


    return render (request, "dashboard\\forget1.html")
def changepassword(request, token):
    user = profile.objects.get(forget_token = token)
    if request.method == "POST":
        userid = request.POST.get('userid')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.success(request, "both Password is not same")
            return redirect('changepassword')
        else :
            user1 = CustomUser.objects.get(userid = userid)
            user1.set_password(password2)
            user1.save()
            return redirect('doLogin')
        
    data = {
        'user' : user
    }

    return render (request, "dashboard\\changepassword.html", data)



def doLogin(request):
    if request.method == "POST":
       user = EmailBackend.authenticate(request,
                                        username=request.POST.get('email'),
                                        password=request.POST.get('password'),)
       if user!=None:
           login(request,user)
           user_type = user.user_type
           if user_type == '1':
               return redirect(reverse('dashboard'))
           elif user_type == '2':
               return redirect(reverse('teacherdashboard'))
           elif user_type == '3':
               return redirect(reverse('studenthome'))
           else:
               messages.error(request,'Email and Password Are Invalid !')
               return redirect('doLogin')
       else:
           messages.error(request,'Email and Password Are Invalid !')
           return redirect('doLogin')
    return render (request, "dashboard\\pages-login.html")

def logout_user(request):
    if request.user != None:
        logout(request)
    return redirect("/")