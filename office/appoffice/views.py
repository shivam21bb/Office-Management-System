from django.shortcuts import render
from .models import Department,Role,Employee
from datetime import datetime
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,'appoffice/index.html')
def all_employee(request):
    emp=Employee.objects.all()
    context={
        'emp':emp 
    }
    return render(request,'appoffice/all_employee.html',context)

def add_employee(request):
    if request.method =="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        salarly=request.POST['salarly']
        bonus=int(request.POST['bonus'])
        phone=int(request.POST['phone'])
        role=int(request.POST['role'])
        dept=int(request.POST['dept'])
        a=Employee(first_name=first_name,last_name=last_name,salarly=salarly,bonus=bonus,phone=phone,role_id=role,dept_id=dept,hire_date=datetime.now())
        a.save()
        return HttpResponse("Employee Added Successfully")
    else:
      return render(request,'appoffice/add_employee.html')
def delete_employee(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Please Enter Valid EMP ID")
    emp=Employee.objects.all()
    context={
    'emp':emp
    }
    return render(request,'appoffice/delete_employee.html',context)

def filter(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)

        context = {
            'emps': emps
        }
        return render(request, 'appoffice/all_employee.html', context)

    elif request.method == 'GET':
        return render(request, 'appoffice/filter.html')
    else:
        return HttpResponse('An Exception Occurred')