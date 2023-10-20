from django.shortcuts import redirect, render 
from django.conf import settings
from django.contrib import messages
from database.models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django.core.mail import send_mail


@login_required(login_url='/dologin/')
def index(request):
    contact = Contact.objects.all().order_by('-id')[:10] 
    notice = Notice.objects.all().order_by('-id')[:5]
    data = {
        'contact': contact,
        'notice': notice,
    }

    return render (request, "dashboard\index.html", data)

@login_required(login_url='/dologin/')
def notice(request):
    if request.method == "POST":
        notice = request.POST.get('notice')
        notice = Notice(
            notice = notice
        )
        notice.save()

        messages.success(request,"Notice is Update")

    notice = Notice.objects.all
    
    data = {
        
        'notice': notice
        
    }
    return render (request, "dashboard\\notice.html",data)

@login_required(login_url='/dologin/')
def welcomepic(request):
    if request.method == "POST":
        
        # adding homepage picture

        homepage_pic = request.FILES.get('homepage_pic')
        
        
        homepagepicture = Homepagepicture(
                homepage_pic = homepage_pic
            )
        homepagepicture.save()

    
    homepicture = Homepagepicture.objects.all
    
    data = {
        'homepicture' : homepicture,
        
       
    }
    messages.success(request,"Picture is added")

    return render (request, "dashboard\\welcomepic.html",data)

@login_required(login_url='/dologin/')
def gallerypic(request):
    if request.method == "POST":
        
        gallery_pic = request.FILES.get('gallery_pic')
        about = request.POST.get('about')
        

        # adding gallery picture
        

        gallery_picture = Gallerypicture(
            gallery_pic = gallery_pic,
            about = about
        )
        gallery_picture.save()


        messages.success(request,"Picture is added")
    
    
    gallerypicture = Gallerypicture.objects.all
    
    data = {
        
        'gallerypicture' :gallerypicture
        
    }

    return render (request, "dashboard\\galleryupdate.html",data)
@login_required(login_url='/dologin/')
def addnotes(request):
    if request.method == "POST":
        
        notes = request.FILES.get('notes')
        subject = request.POST.get('subject')
        study = request.POST.get('study')
        about = request.POST.get('about')
        

        # adding gallery picture
        

        notes = Notes(
            Notes = notes,
            Subject = subject,
            study = study,
            about = about,
        )
        notes.save()


        messages.success(request,"Notes is added")
    
    
    notes = Notes.objects.all
    
    data = {
        
        'notes' :notes
        
    }

    return render (request, "dashboard\\notes.html",data)

@login_required(login_url='/dologin/')
def teacherpic(request):
    if request.method == "POST":
        
        name = request.POST.get('name')
        qual = request.POST.get('qual')
        tpic = request.FILES.get('tpic')
        

        teacherpicture = Teacherpicture(
            name = name,
            qualification = qual,
            teacher_pic = tpic
        )
        teacherpicture.save()

        messages.success(request,"Picture is added")

    teacher_picture = Teacherpicture.objects.all
    
    data = {
        
        'teacher_picture':teacher_picture
        
    }

    return render (request, "dashboard\\teacherupdate.html",data)


@login_required(login_url='/dologin/')
def testimonial(request):
    if request.method == "POST":
        name = request.POST.get('name')
        Feedback = request.POST.get('feedback')
        
        

        testinomial = Testinomial(
            name = name,
            feedback = Feedback
        )
        testinomial.save()

        messages.success(request,"Picture is added")

    testino = Testinomial.objects.all
    
    data = {
        
        'testinomial':testino
        
    }

    return render (request, "dashboard\\testinomial.html",data)


@login_required(login_url='/dologin/')
def topperupdate(request):
    if request.method == "POST":
        name = request.POST.get('name')
        study = request.POST.get('study')
        school = request.POST.get('school')
        marks = request.POST.get('marks')
        tphoto = request.FILES.get('tphoto')

        topper_1 = Tophomepage(
            name = name,
            topper_pic = tphoto,
            study = study,
            school = school,
            marks = marks

        )
        topper_1.save()

        messages.success(request,"Topper of the Month is Update")

    topper = Tophomepage.objects.all
    
    data = {
        
        'topper': topper
        
    }
    
    return render (request, "dashboard\\tupdate.html",data)


@login_required(login_url='/dologin/')
def topperbupdate(request):
    if request.method == "POST":
        name = request.POST.get('name')
        study = request.POST.get('study')
        school = request.POST.get('school')
        marks = request.POST.get('marks')
        tphoto = request.FILES.get('tphoto')
        
        topper_1 = Topbackpage(
            name = name,
            topper_pic = tphoto,
            study = study,
            school = school,
            marks = marks

        )
        topper_1.save()

        messages.success(request,"Topper of the Month is Update")

    topper = Topbackpage.objects.all
    
    data = {
        
        'topper': topper
        
    }
    
    return render (request, "dashboard\\tbupdate.html",data)


@login_required(login_url='/dologin/')
def addstudent(request):
    if CustomUser.objects.count() == 0 :

        userid = 10001
    else :
        userid = CustomUser.objects.aggregate(max = Max('userid'))['max']+1

    
    

    if request.method == 'POST':
        userid = request.POST.get('userid')
        name = request.POST.get('name')
        study = request.POST.get('study')
        joinyear = request.POST.get('joinyear')
        dob = request.POST.get('dob')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        parentphone = request.POST.get('parentphone')
        password = request.POST.get('Password')
    
        if CustomUser.objects.filter(email=email).exists() :

            messages.warning(request,'Email Is Already Taken')
            return redirect('addstudent')
        else:
            user = CustomUser(
                email = email,
                user_type = 3,
                userid = userid,
                username=userid
            )
            user.set_password(password)
            user.save()

            student = Student(
                userid = user,
                name = name,
                Study = study,
                yearofjoin = joinyear,
                dob = dob,
                personalphnoe = phone,
                parentphone = parentphone

            )
            student.save()


            send_mail(
            "Subject here",
            "Here is the message.",
            "djangomail2345@gmail.com",
            [email],
            fail_silently=False,
)


    data = {
        
        'userid': userid
        
    }


    return render (request, "dashboard\\addstudent.html",data)

@login_required(login_url='/dologin/')
def addteacher(request):

    if CustomUser.objects.count() == 0 :

        userid = 10001
    else :
        userid = CustomUser.objects.aggregate(max = Max('userid'))['max']+1

    if request.method == 'POST':
        userid = request.POST.get('userid')
        name = request.POST.get('name')
        qual = request.POST.get('qual')
        joinyear = request.POST.get('joinyear')
        dob = request.POST.get('dob')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('Password')
    
        if CustomUser.objects.filter(email=email).exists() :

            messages.warning(request,'Email Is Already Taken')
            return redirect('addteacher')
        else:
            user = CustomUser(
                email = email,
                user_type = 2,
                userid = userid,
                username=userid
            )
            user.set_password(password)
            user.save()

            teacher = Teacher(
                userid = user,
                name = name,
                qual = qual,
                yearofjoin = joinyear,
                dob = dob,
                personalphnoe = phone,

            )
            teacher.save()
            messages.warning(request,'Teacher is register please reload for next entry')
            

    data = {
        
        'userid': userid
        
    }

    return render(request, "dashboard\\addteacher.html",data)