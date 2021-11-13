from django.db import models

# Create your models here.
class EmpTable(models.Model):
    
    id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length = 200,null=True)
    employee_email = models.CharField(max_length =200,null=True)
  
    
    
    def __str__(self):
        return self.employee_name