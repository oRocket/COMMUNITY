from django.contrib import admin
from .models import Incident, Leader, Profile

# Register the Incident model
admin.site.register(Incident)
admin.site.register(Leader)
admin.site.register(Profile)
# admin.site.register(Member)
