# Generated by Django 5.1.1 on 2024-09-17 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0008_remove_incident_user_alter_incident_reported_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='incident_type',
            field=models.CharField(choices=[('theft', 'Theft'), ('vandalism', 'Vandalism'), ('fire', 'Fire'), ('accident', 'Accident'), ('emergency', 'Emergency'), ('medical', 'Medical'), ('police', 'Police'), ('other', 'Other')], default='other', max_length=100),
        ),
    ]