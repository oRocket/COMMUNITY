from django.contrib.auth import logout
from django.utils import timezone
from django.conf import settings
from datetime import datetime

class InactivityLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Get the last activity time
            last_activity = request.session.get('last_activity')
            if last_activity:
                # Convert string back to datetime
                last_activity = datetime.fromisoformat(last_activity)
                # Calculate the time since last activity
                if (timezone.now() - last_activity).total_seconds() > settings.SESSION_COOKIE_AGE:
                    logout(request)  # Log out the user if inactive for too long
            # Update last activity time
            request.session['last_activity'] = timezone.now().isoformat()  # Store as ISO format string

        response = self.get_response(request)
        return response
