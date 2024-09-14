from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from reports.models import Incident

class Command(BaseCommand):
    help = 'Creates Community Leaders group with necessary permissions'

    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name='Community Leaders')
        if created:
            self.stdout.write(self.style.SUCCESS('Successfully created Community Leaders group'))
        else:
            self.stdout.write(self.style.WARNING('Community Leaders group already exists'))

        # Get content type for the Incident model
        incident_content_type = ContentType.objects.get_for_model(Incident)

        # Define permissions
        permissions = [
            'view_incident',
            'change_incident',
        ]

        # Add permissions to the group
        for permission_codename in permissions:
            permission = Permission.objects.get(
                codename=permission_codename,
                content_type=incident_content_type
            )
            group.permissions.add(permission)

        self.stdout.write(self.style.SUCCESS('Successfully added permissions to Community Leaders group'))
