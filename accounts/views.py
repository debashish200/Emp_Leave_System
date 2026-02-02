from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from leaves.models import LeaveBalance
# Create your views here.

@login_required
def dashboard(request):
    balance = LeaveBalance.objects.filter(user=request.user).first()
    return render(request, 'dashboard.html', {'balance': balance})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')