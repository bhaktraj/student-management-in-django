"""institue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from institue import views , hodviews, Studentviews , teacherviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('about/', views.about),
    path('event/', views.event),
    path('teacher/', views.teacher),
    path('contact/', views.contact, name='contact'),
    path('notes/', views.notes, name='notes'),
    path('course/', views.course),
    path('topper/', views.topper),
    path('result/', views.result),
    path('resultdetails/', views.search, name='search'),
    path('foundation/', views.foundation),
    path('1112th/', views.eleven),
    path('jeedetails/', views.jeedetails),
    path('neetdetails/', views.neetdetails),
    


    #hod Url\\\\\\\\\\\\\\\\\\\\\\\\
    path('hod/', hodviews.index, name='dashboard'),
    path('notice/', hodviews.notice, name='notice'),
    path('welcomepic/', hodviews.welcomepic, name='welcomepic'),
    path('galleryupdate/', hodviews.gallerypic, name='galleryupdate'),
    path('teacherupdate/', hodviews.teacherpic, name='teacherupdate'),
    path('testimonialupdate/', hodviews.testimonial, name='testimonialupdate'),
    path('topperupdate/', hodviews.topperupdate, name='tupdate'),
    path('topperbupdate/', hodviews.topperbupdate, name='tbupdate'),
    path('addstudent/', hodviews.addstudent, name='addstudent'),
    path('addteacher/', hodviews.addteacher, name='addteacher'),
    path('addnotes/', hodviews.addnotes, name='addnotes'),

    #teacher url\\\\\\\\\\\\\\\\\\\\\\
    path('teacheradmin/', teacherviews.index, name='teacherdashboard'),
    path('teacherprofile/', teacherviews.profile, name='teacherprofile'),
    path('marksupdate/', teacherviews.marksupdate, name='marksupdate'),


    #Student Url\\\\\\\\\\\\\\\\\\\\\
    path('student/', Studentviews.index, name='studenthome'),
    path('myprofile/', Studentviews.profile, name='myprofile'),
    path('myprofilepassword/', Studentviews.profilepassword, name='myprofilepassword'),

    #login url\\\\\\\\\\\\\\\\\\\\\\\
    
    path('dologin/', views.doLogin, name='doLogin'),
    path('verify/', views.verifyuserid, name='verify'),
    path('changepassword/<token>/', views.changepassword, name='changepassword'),
    path('dologout/', views.logout_user, name='doLogout')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
