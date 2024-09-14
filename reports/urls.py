from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  # Home page with incident form
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard for logged-in users
    path('incident/<int:incident_id>/', views.incident_detail, name='incident_detail'),  # Incident detail page
    path('report/', views.report_incident, name='report_incident'),  # Incident reporting page
    path('register/', views.register, name='register'),  # User registration page
    path('login/', auth_views.LoginView.as_view(template_name='reports/login.html'), name='login'),  # Login page
    path('logout/', views.logout_view, name='logout'),  # Logout page
    path('leader-dashboard/', views.leader_dashboard, name='leader_dashboard'),
    path('review-report/<int:incident_id>/', views.review_report, name='review_report'),
]
