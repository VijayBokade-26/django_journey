from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .forms import StudentsForm


from .models import Students
# Create your views here.

def Hello_world(request):
    return render(request, "home.html")

def Student_form(request):
    if request.method == "POST":
        form = StudentsForm(request.POST, request.FILES)
        print("^^^^^^^^^", form.errors)
        if form.is_valid():
            form.save()
            return redirect("students_list") 
        else:
            return render(request, 'home.html',{'form': form})
    else:
        form = StudentsForm() 
        return render(request, 'home.html',{'form': form})

def student_listing(request):
    stud = Students.objects.all()
    return render(request, "students_list.html", {"stud":stud})

def students_edit(request, id):
    stu_obj = get_object_or_404(Students, pk = id)
    if request.method == "POST":    
        print("!!!!!!!")
        stud_ent =  StudentsForm(request.POST, request.FILES,instance = stu_obj )
        if stud_ent.is_valid():
            stud_ent.save()
            return redirect("students_list")
    else:
        print("@@@@@@",stu_obj)
        stud_ent =  StudentsForm(instance = stu_obj )
            # request.POST, request.FILES,
    return render(request, "edit_form.html", {"form":stud_ent})


def deleteview(request, id):
    stud_obj = get_object_or_404(Students,pk = id)
    if stud_obj:
        stud_obj.delete()
    return redirect("students_list")