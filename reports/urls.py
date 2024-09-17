from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import incident_list, edit_incident, delete_incident, report_incident, incident_detail

urlpatterns = [
    path('', views.home, name='home'),  # Home page with incident form
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard for logged-in users
    path('incident/', incident_list, name='incident_list'),  # Add this line
    path('incident/<int:incident_id>/', incident_detail, name='incident_detail'),  # Incident detail page
    path('incident/<int:incident_id>/edit/', edit_incident, name='edit_incident'),
    path('incident/<int:incident_id>/delete/', delete_incident, name='delete_incident'),
    path('report/', report_incident, name='report_incident'),  # Incident reporting page
    path('register/', views.register, name='register'),  # User registration page
    path('login/', auth_views.LoginView.as_view(template_name='reports/login.html'), name='login'),  # Login page
    path('logout/', views.logout_view, name='logout'),  # Logout page
    path('leader-dashboard/', views.leader_dashboard, name='leader_dashboard'),
    path('review-report/<int:incident_id>/', views.review_report, name='review_report'),
]
