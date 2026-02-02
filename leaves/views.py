from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.http import JsonResponse
from datetime import timedelta


# Create your views here.
@login_required
def leave_request(request):
    if request.method=='POST':
        form=LeaveRequestForm(request.POST)
        if form.is_valid():
            leave=form.save(commit=False)
            leave.user=request.user
            leave.save()
            return redirect('dashboard')
    else:
        form=LeaveRequestForm()
    return render(request,'leave_request.html',{'form':form})

@login_required
def approve_leave(request):
    leaves = LeaveRequest.objects.filter(status='PENDING')

    if request.method == 'POST':
        leave = LeaveRequest.objects.get(id=request.POST.get('leave_id'))
        form = LeaveApprovalForm(request.POST, instance=leave)

        if form.is_valid():
            leave = form.save()
            balance, created = LeaveBalance.objects.get_or_create(
                user=leave.user,
                defaults={
                    'vacation': 20,
                    'sick': 10
                }
            )
            if leave.status == "APPROVED":
                days = (leave.end_date - leave.start_date).days + 1

                #print("Leave type:", leave.leave_type)

                if leave.leave_type == 'VACATION':
                    balance.vacation -= days
                elif leave.leave_type == 'SICK':
                    balance.sick -= days
                #print("Before:", balance.vacation, balance.sick)
                balance.save()
                #print("After:", balance.vacation, balance.sick)
        return redirect('approve_leave')
    approval_form = LeaveApprovalForm()
    return render(request, 'leave_approval.html', {
        'leaves': leaves,
        'form': approval_form
    })



@login_required
def leave_calendar(request):
    return render(request, 'calendar.html')

@login_required
def leave_calendar(request):
    approved_leaves = LeaveRequest.objects.filter(status='APPROVED')
    return render(request, 'calendar.html', {'leaves': approved_leaves})


@login_required
def leave_events(request):
    events = []

    leaves = LeaveRequest.objects.filter(status='APPROVED')

    for leave in leaves:
        events.append({
            'title': f"{leave.user.username} ({leave.leave_type})",
            'start': leave.start_date.strftime('%Y-%m-%d'),
            'end': (leave.end_date + timedelta(days=1)).strftime('%Y-%m-%d'),
            'color': '#28a745', 
        })

    return JsonResponse(events, safe=False)
