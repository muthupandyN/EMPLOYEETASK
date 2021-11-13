from django.urls import path
from .import views


urlpatterns = [

    path('',views.adminLogin,name='login'),
    path('logout/',views.adminlogout,name='admin_logout'),
    path('emplyee/',views.adminEmployee,name='admin_employee'),
    path('employeesave/',views.employeeSave,name='employee_save'),
    path('employeeList/',views.employeeList,name='employee_list'),
    path('employeeupdate/',views.employeeUpdate,name='employee_update'),
    path('employeeUpdatesave/',views.employeeUpdateSave,name='emp_updatesave'),
    path('empdelete/',views.employeeDelete,name='emp_delte')
]