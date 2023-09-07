from django.shortcuts import render

# Create your views here.

from app.models import *

from django.http import HttpResponse
def insert_school(request):
    if request.method=='POST':
        #request.POST={'scn':SV,'sp':SV,'sl':SV}
        scn=request.POST['scn']
        sp=request.POST['sp']
        sl=request.POST['sl']

        SO=School.objects.get_or_create(ScName=scn,ScPrincipal=sp,ScLocation=sl)[0]
        SO.save()
        QLSO=School.objects.all()
        d={'QLSO':QLSO}
        return render(request,'display_schools.html',d)
    
    return render(request,'insert_school.html')



''' if request.method=='POST':
    sc=
    sn=
    si=

    SO=School.objects.get(ScName=sc)

    STO=Student.objects.get_or_create(Scname=SO,Sname=sn,Sid=si)[0]
    STO.save()
'''

