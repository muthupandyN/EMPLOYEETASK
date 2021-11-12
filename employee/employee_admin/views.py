from django.shortcuts import render,redirect

# Create your views here.


def adminLogin(request):
    return render(request, 'employee_admin/adminlogin.html')