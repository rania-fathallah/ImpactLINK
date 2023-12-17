from django.shortcuts import render, redirect, get_object_or_404
from .models import Evenement
from login.models import EmployeeAccount
from django.contrib.auth.decorators import login_required


def liste_evenements(request):
    evenements = Evenement.objects.all()
    return render(request, "liste_evenements.html", {"evenements": evenements})

@login_required
def join_event(request, pk):
    employee = request.user  # The logged-in user
    evenement = get_object_or_404(Evenement, pk=pk)
    
    evenement.participants.add(employee)
    return redirect('evenements:liste_evenements')