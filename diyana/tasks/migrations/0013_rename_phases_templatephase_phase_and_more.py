# Generated by Django 4.1 on 2023-10-05 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_remove_template_phases_template_phases'),
    ]

    operations = [
        migrations.RenameField(
            model_name='templatephase',
            old_name='phases',
            new_name='phase',
        ),
        migrations.RenameField(
            model_name='templatephase',
            old_name='templates',
            new_name='template',
        ),
        migrations.RemoveField(
            model_name='template',
            name='phases',
        ),
    ]
