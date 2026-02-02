from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class LeaveBalance(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    vacation = models.IntegerField(default=20)
    sick = models.IntegerField(default=10)

    def __str__(self):
        return self.user.username
    
class LeaveRequest(models.Model):
    STATUS = (
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=20)
    start_date=models.DateField()
    end_date=models.DateField()
    reason=models.TextField()
    status=models.CharField(max_length=20,choices=STATUS,default='PENDING')
    manager_comment = models.TextField(blank=True)

