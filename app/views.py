from django.shortcuts import render
from django.http import HttpResponse
from data.models import data
def home(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        rno=request.POST['rno']
        department=request.POST['department']
        problem=request.POST['problem']
        description=request.POST['des']
        var=data(fname=fname,lname=lname,rno=rno,dept=department,problem=problem,desc=description)
        var.save()
        return render(request,"success.html")
    return render(request,"index.html")
    
