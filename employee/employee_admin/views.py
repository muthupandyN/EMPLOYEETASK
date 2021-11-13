from django.shortcuts import render,redirect
from django.contrib import messages

# Create your views here.


from django.contrib.auth.models import User, auth    
from django.contrib import messages
from .models import EmpTable
from django.contrib.auth.decorators import login_required

def adminLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("admin_employee")
        else:
            messages.info(request, '*Invalid username or password*')
            return redirect('login')

    else:
        return render(request, 'employee_admin/adminlogin.html')    



def adminlogout(request):
    auth.logout(request)
    return redirect('login')  

@login_required(login_url="/admin/")
def adminEmployee(request):
    return render(request,'employee_admin/employee.html')

@login_required(login_url="/admin/")
def employeeSave(request):
    if request.method == 'POST':

        employee_name = request.POST.get('employee_name')
        employee_email= request.POST.get('emp_email')
        EmpTable(employee_name=employee_name, employee_email=employee_email).save()
        messages.success(request, '*Successfully Saved Data*')
        return redirect('admin_employee')    
@login_required(login_url="/admin/")
def employeeList(request):

    emp_datas = EmpTable.objects.all()

    return render(request, 'employee_admin/employee_list.html', {"emp_datas": emp_datas})   
@login_required(login_url="/admin/")

def employeeUpdate(request):
    id = request.GET.get("id")
    emp_data = EmpTable.objects.filter(id=id)
    return render(request, 'employee_admin/update_emp.html', {"emp_data":emp_data })
@login_required(login_url="/admin/")

def employeeUpdateSave(request):
    # print('check')
    id = request.GET.get('id')
    employee_name = request.POST.get('employee_name')
    employee_email= request.POST.get('emp_email')
    EmpTable.objects.filter(id=id).update(employee_name=employee_name, employee_email=employee_email)
    messages.success(request, '*Successfully Updated Data*')
    return redirect('employee_list')  

@login_required(login_url="/admin/")
def employeeDelete(request):

    id = request.GET.get('id')    
    emp_obj = EmpTable.objects.get(id=id)
    emp_obj.delete()

    return redirect('employee_list')

def employeeSearch(request):

    employee_name =  request.POST.get('employee_name')
    print(type(employee_name))
    if(employee_name.isalpha()):
        
        emp_obj = EmpTable.objects.filter(employee_name__icontains=employee_name)
        # print(emp_obj)
        
        context = {
            "emp_datas":emp_obj
        }
        return render(request,'employee_admin/employeesearch.html',context)
    
    elif(employee_name. isalnum()):
        id =int(employee_name)
        emp_obj = EmpTable.objects.filter(id=id)
        # print(emp_obj)
        
        context = {
            "emp_datas":emp_obj
        }
        return render(request,'employee_admin/employeesearch.html',context)

    else:
        return redirect('employee_list')    




     
                