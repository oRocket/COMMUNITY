from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Incident
from .forms import CustomUserCreationForm, IncidentForm  # Import both forms

# Home page view
def home(request):
    latest_incidents = Incident.objects.order_by('-date_reported')[:5]  # Get the 5 most recent incidents
    return render(request, 'reports/home.html', {
        'latest_incidents': latest_incidents,
        'is_authenticated': request.user.is_authenticated,
    })

# Incident reporting view
@login_required
def report_incident(request):
    if request.method == 'POST':
        incident = Incident()
        form = IncidentForm(request.POST, instance=incident)
        if form.is_valid():
            incident.reported_by = request.user  # Ensure the user is set
            incident.save()
            return redirect('home')
    else:
        form = IncidentForm()
    return render(request, 'reports/report_incident.html', {'form': form})

# Dashboard view
@login_required
def dashboard(request):
    incidents = Incident.objects.all()
    return render(request, 'reports/dashboard.html', {'incidents': incidents})

# Incident detail view
def incident_detail(request, incident_id):
    if not request.user.is_authenticated:
        return redirect('login')
    incident = Incident.objects.get(pk=incident_id)
    return render(request, 'reports/incident_detail.html', {'incident': incident})

# User registration view
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Save additional fields
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.profile.middle_name = form.cleaned_data['middle_name']
            user.profile.date_of_birth = form.cleaned_data['date_of_birth']
            user.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'reports/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'reports/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def is_community_leader(user):
    return user.groups.filter(name='Community Leaders').exists()

@user_passes_test(is_community_leader)
def leader_dashboard(request):
    pending_reports = Incident.objects.filter(status='pending')
    active_reports = Incident.objects.filter(status__in=['approved', 'escalated'])
    resolved_reports = Incident.objects.filter(status='resolved')

    context = {
        'pending_reports': pending_reports,
        'active_reports': active_reports,
        'resolved_reports': resolved_reports,
    }
    return render(request, 'reports/leader_dashboard.html', context)

@user_passes_test(is_community_leader)
def review_report(request, incident_id):
    incident = get_object_or_404(Incident, id=incident_id)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action in ['approve', 'reject', 'escalate', 'resolve']:
            incident.status = action + 'd' if action != 'resolve' else 'resolved'
            incident.reviewed_by = request.user
            incident.save()
            # TODO: Add logic to send email/SMS for escalation
        return redirect('leader_dashboard')
    return render(request, 'reports/review_report.html', {'incident': incident})