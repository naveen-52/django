from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

# Create your views here.

def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students':students})

def add(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        department = request.POST['department']

        Student.objects.create(
            name = name,
            age = age,
            department = department
        )

        return redirect('/')
    return render(request, 'add.html')

def edit(request, id):
    student = get_object_or_404(Student, id = id)

    if request.method == 'POST':
        student.name = request.POST['name']
        student.age = request.POST['age']
        student.department = request.POST['department']

        student.save()
        return redirect('/')
    return render(request, 'edit.html', {'student':student})

def delete(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('/')
