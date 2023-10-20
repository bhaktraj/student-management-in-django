from django.shortcuts import get_object_or_404, render
from database.models import *
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage



@login_required(login_url='/dologin/')
def index(request):
    student = get_object_or_404(Student, userid=request.user)
    
    subject = Subject.objects.filter(userid=student.userid)
    data = {
        'student':student,
        'subject':subject
    }


    return render (request, "dashboard\Studenthome.html",data )


@login_required(login_url='/dologin/')
def profile(request):
    student = get_object_or_404(Student, userid=request.user)

    user1 = CustomUser.objects.get(userid=request.user.userid)
    

    if request.method == 'POST':
        name = request.POST.get('name')
        study = request.POST.get('class')
        school = request.POST.get('school')
        phone = request.POST.get('phone')
        profile_pic = request.FILES.get('profile_pic') or None
        password1 = request.POST.get('password') or None
        password2 = request.POST.get('renewpassword') or None

        
        if password1 != None:
            user1.set_password(password1)
                    
        
        
        if profile_pic != None:
                   # fs = FileSystemStorage()
                   # filename = fs.save(profile_pic.name, profile_pic)
                   # passport_url = fs.url(filename)
                    student.profile_pic = profile_pic

        student.name = name
        student.Study = study
        student.school = school
        student.personalphnoe = phone
        student.save()
        user1.save()

        

        
    data = {
        'student':student,
        
    }
    return render (request, "dashboard\Studentprofile.html",data)

login_required(login_url='/dologin/')
def profilepassword(request):
    student = get_object_or_404(Student, userid=request.user)

    user1 = CustomUser.objects.get(userid=request.user.userid)
    

    if request.method == 'POST':
        password1 = request.POST.get('password') or None
        password2 = request.POST.get('renewpassword') or None

        
        if password1 != None:
            user1.set_password(password1)
                    
        
        
        
        user1.save()

        

        
    data = {
        'student':student,
        
    }
    return render (request, "dashboard\Studentprofile.html",data)