from django import forms 
from .models import LeaveRequest

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model=LeaveRequest
        fields=['leave_type','start_date','end_date','reason']
        widgets = {
                'leave_type': forms.Select(choices=[('VACATION', 'Vacation'),('SICK', 'Sick'),('Casual','Casual')]),
                'start_date': forms.DateInput(attrs={'type': 'date'}),
                'end_date': forms.DateInput(attrs={'type': 'date'}),
                'reason': forms.Textarea(attrs={'rows': 3}),
            }

class LeaveApprovalForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['status', 'manager_comment']
        widgets = {
            'status': forms.Select(choices=[('APPROVED','Approve'),('REJECTED','Reject')]),
            'manager_comment': forms.Textarea(attrs={'rows': 2}),
        }