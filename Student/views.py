from django.shortcuts import redirect, render
from .forms import *
from .models import *
from django.contrib import messages
# Create your views here.


def all_students(request):
    students = Students.objects.all()
    # for std in students:
        # try:
        #     print(std.instruments.name)
        # except:
        #     print("nothing")
    context = {
        'students' : students
    }
    return render(request, 'index.html', context)


def add_student(request):
    if request.method == "GET":
        form = StudentForm()
        form2 = StudentInstrumentsForm()
        form2.fields['student'].widget = forms.HiddenInput()
        context = {
            'form' : form,
            'form2' : form2,
        }
        return render(request, 'add_student.html',context)
    else:
        form = StudentForm(request.POST)
        form2 = StudentInstrumentsForm(request.POST)
        if form.is_valid() and form2.is_valid():
            instance = form.save()
            instrument = form2.save(commit=False)
            instrument.student = instance
            instrument.save()
            messages.success(request, 'Student added successfully')
            return redirect('home')
            # return render(request, 'index.html')
        else:
            print(form.errors)


def delete_student(request, id):
    try:
        student = Students.objects.get(id=id).delete()
    except Students.DoesNotExist:
        return redirect('home')
    messages.success(request, 'Student deleted successfully')
    return redirect('home')


def update_student(request, id=None):
    try:
        student = Students.objects.get(id=id)
    except Students.DoesNotExist:
        return redirect('home')
    if request.method == 'GET':
        form = StudentForm(instance=student)

        form2 = StudentInstrumentsForm(instance=student.instruments)
        form2.fields['student'].widget = forms.HiddenInput()

        context = {'form' : form, 'form2' : form2, "student" : student}
        return render(request, 'update_student.html', context)
    else:
        form = StudentForm(request.POST, instance=student)
        form2 = StudentInstrumentsForm(request.POST, instance=student.instruments)

        if form.is_valid() and form2.is_valid():
            instance = form.save()
            instrument = form2.save(commit=False)
            instrument.student = instance
            instrument.save()
            messages.success(request, 'Student updated successfully')
        return redirect('home')