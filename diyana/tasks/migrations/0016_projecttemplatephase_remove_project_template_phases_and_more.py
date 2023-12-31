# Generated by Django 4.1 on 2023-10-05 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0015_alter_templatephase_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectTemplatePhase',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL)),
                ('phase', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tasks.phase')),
            ],
            options={
                'db_table': 'tasks_project_template_phase',
            },
        ),
        migrations.RemoveField(
            model_name='project',
            name='template_phases',
        ),
        migrations.AddField(
            model_name='project',
            name='phases',
            field=models.ManyToManyField(related_name='projects', through='tasks.ProjectTemplatePhase', to='tasks.phase'),
        ),
        migrations.AddField(
            model_name='project',
            name='templates',
            field=models.ManyToManyField(related_name='projects', through='tasks.ProjectTemplatePhase', to='tasks.template'),
        ),
        migrations.AlterField(
            model_name='template',
            name='phases',
            field=models.ManyToManyField(related_name='template', through='tasks.ProjectTemplatePhase', to='tasks.phase'),
        ),
        migrations.DeleteModel(
            name='TemplatePhase',
        ),
        migrations.AddField(
            model_name='projecttemplatephase',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tasks.project'),
        ),
        migrations.AddField(
            model_name='projecttemplatephase',
            name='template',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tasks.template'),
        ),
        migrations.AddField(
            model_name='projecttemplatephase',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL),
        ),
    ]
