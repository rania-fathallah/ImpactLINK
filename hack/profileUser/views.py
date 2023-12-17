from django.shortcuts import render, get_object_or_404, redirect
from login.models import EmployeeAccount
from django.contrib.auth.decorators import login_required
from .models import Certification
from django.http import HttpResponseBadRequest
from .models import Profile


@login_required
def profile_view(request):
    profile = get_object_or_404(EmployeeAccount, matricule=request.user.matricule)
    return render(request, 'profile.html', {'profile': profile})



@login_required
def certification_list(request):
    profile = request.user.profile 
    certifications = profile.certifications.all() 
    return render(request, 'certification_list.html', {'certifications': certifications})



@login_required
def add_certification(request):

    if request.method == 'POST':
        certificate = request.POST.get('certificate')
        platforme = request.POST.get('platforme')
        dateD = request.POST.get('d')
        pdf_file = request.FILES.get('pdf_file')


        #if not (certificate and platforme and dateD and pdf_file):
        #    return HttpResponseBadRequest("Invalid form data"+ dateD)

        employee_account = get_object_or_404(EmployeeAccount, matricule=request.user.matricule)
        profile = get_object_or_404(Profile, employee_account=employee_account)

        #profile = Profile.objects.get(employee_account__user)
        
        certification = Certification(certificate=certificate, platforme=platforme, dateD = dateD, pdf_file = pdf_file)
        certification.save()
        
        profile.certifications.add(certification)
                
        return redirect("profiles:certification_list")

    return render(request, "add_certification.html")
    


@login_required
def update_certification(request, pk):
    certification = get_object_or_404(Certification, pk=pk)
    if request.method == 'POST':
        certification.certificat = request.POST.get('certificat')
        certification.prenom = request.POST.get('platform')
        certification.date = request.POST.get('date')

        certification.save()
        return redirect('liste_certifications')
    return render(request, 'update_certification.html')


@login_required
def delete_certification(request, pk):
    certification = get_object_or_404(Certification, pk=pk)
    certification.delete()
    return redirect('liste_certifications')

