from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Incident

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    middle_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    date_of_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'middle_name', 'last_name', 'email', 'date_of_birth', 'password1', 'password2')

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['title', 'description', 'location', 'status', 'incident_type', 'date_occurred']  # Include date_occurred
        widgets = {
            'date_occurred': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'step': '2'  # Allows for seconds input
            }),
        }

# Add a new form for editing incidents
class EditIncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['title', 'description', 'location', 'status', 'incident_type', 'date_occurred']
        

# neighborhood_watch/reports/forms.py
from django import forms
from .models import Incident

class IncidentStatusForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['status']