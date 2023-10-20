from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from database.models import *

@login_required(login_url='/dologin/')
def index(request):
    teacher = get_object_or_404(Teacher, userid=request.user)

    
   
    data = {
        'teacher':teacher,
        
    }

    return render (request, "dashboard\Teacherhome.html",data )

@login_required(login_url='/dologin/')
def profile(request):
    
    return render (request, "dashboard\Teacherprofile.html")

@login_required(login_url='/dologin/')
def marksupdate(request):


    if request.method == 'POST':

        userid = request.POST.get('userid')
        english = request.POST.get('english')
        math = request.POST.get('math')
        science = request.POST.get('science')
        sscience = request.POST.get('sscience')

        user = CustomUser.objects.get(userid = userid)

    

        subject = Subject.objects.create(userid = user, english = english,math=math,science=science,socialscience=sscience)


        
    return render (request, "dashboard\marksupdate.html")