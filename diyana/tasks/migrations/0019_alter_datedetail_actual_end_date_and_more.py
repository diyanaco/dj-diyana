# Generated by Django 4.1 on 2023-10-05 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0018_alter_projecttemplatephase_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datedetail',
            name='actual_end_date',
            field=models.DateTimeField(null=True, verbose_name='actual end date'),
        ),
        migrations.AlterField(
            model_name='datedetail',
            name='actual_start_date',
            field=models.DateTimeField(null=True, verbose_name='actual start date'),
        ),
        migrations.AlterField(
            model_name='datedetail',
            name='due_date',
            field=models.DateTimeField(null=True, verbose_name='due date'),
        ),
        migrations.AlterField(
            model_name='datedetail',
            name='reported_date',
            field=models.DateTimeField(null=True, verbose_name='reported date'),
        ),
        migrations.AlterField(
            model_name='datedetail',
            name='start_date',
            field=models.DateTimeField(null=True, verbose_name='start date'),
        ),
        migrations.AlterField(
            model_name='grouptask',
            name='phase',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='groups', to='tasks.phase'),
        ),
    ]