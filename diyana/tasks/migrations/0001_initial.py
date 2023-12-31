# Generated by Django 4.1 on 2023-09-30 11:40

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=150)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'auth_user',
            },
        ),
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('from_type', models.CharField(choices=[('CONSTANT', 'Constant'), ('STATUS', 'Status'), ('PROJECT_TYPE', 'Project Type')], max_length=100)),
                ('value_str', models.CharField(max_length=100)),
                ('value_int', models.IntegerField(default=0)),
                ('value_bool', models.BooleanField()),
                ('created_by', models.ForeignKey(null=True, on_delete=models.SET_NULL, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=models.SET_NULL, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DateDetail',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('from_type', models.CharField(choices=[('SUB_TASK', 'Subtask'), ('TASK', 'Task'), ('GROUP_TASK', 'Group task'), ('MILESTONE', 'Milestone Type'), ('PHASE', 'Phase')], max_length=100)),
                ('due_date', models.DateTimeField(verbose_name='due date')),
                ('start_date', models.DateTimeField(verbose_name='start date')),
                ('reported_date', models.DateTimeField(verbose_name='reported date')),
                ('actual_start_date', models.DateTimeField(verbose_name='actual start date')),
                ('actual_end_date', models.DateTimeField(verbose_name='actual end date')),
                ('created_by', models.ForeignKey(null=True, on_delete=models.SET_NULL, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=models.SET_NULL, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupTask',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_by', models.ForeignKey(null=True, on_delete=models.SET_NULL, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL)),
                ('date_detail', models.ForeignKey(null=True, on_delete=models.SET_NULL, to='tasks.datedetail')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_by', models.ForeignKey(null=True, on_delete=models.SET_NULL, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL)),
                ('date_detail', models.ForeignKey(null=True, on_delete=models.SET_NULL, to='tasks.datedetail')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('urgency', models.IntegerField(default=0)),
                ('gravity', models.IntegerField(default=0)),
                ('criticality', models.IntegerField(default=0)),
                ('value_int', models.IntegerField(default=0)),
                ('value_str', models.CharField(choices=[('LOW', 'Low'), ('LOW_MEDIUM', 'Low Medium'), ('MEDIUM', 'Medium'), ('MEDIUM_HIGH', 'Medium High'), ('HIGH', 'High')], max_length=100)),
                ('created_by', models.ForeignKey(null=True, on_delete=models.SET_NULL, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=models.SET_NULL, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('code', models.ForeignKey(null=True, on_delete=models.SET_NULL, to='tasks.code')),
                ('created_by', models.ForeignKey(null=True, on_delete=models.SET_NULL, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=models.SET_NULL, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('created_by', models.ForeignKey(null=True, on_delete=models.SET_NULL, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=models.SET_NULL, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('assigned_to', models.ForeignKey(null=True, on_delete=models.SET_NULL, related_name='task_assigned_to', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(null=True, on_delete=models.SET_NULL, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL)),
                ('date_detail', models.ForeignKey(null=True, on_delete=models.SET_NULL, to='tasks.datedetail')),
                ('group', models.ForeignKey(null=True, on_delete=models.SET_NULL, to='tasks.grouptask')),
                ('priority', models.OneToOneField(null=True, on_delete=models.SET_NULL, to='tasks.priority')),
                ('reported_by', models.ForeignKey(null=True, on_delete=models.SET_NULL, related_name='task_reported_by', to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(null=True, on_delete=models.SET_NULL, to='tasks.code')),
                ('tag', models.ForeignKey(null=True, on_delete=models.SET_NULL, to='tasks.tag')),
                ('updated_by', models.ForeignKey(null=True, on_delete=models.SET_NULL, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subtask',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('assigned_to', models.ForeignKey(null=True, on_delete=models.SET_NULL, related_name='subtask_assigned_to', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(null=True, on_delete=models.SET_NULL, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL)),
                ('date_detail', models.ForeignKey(null=True, on_delete=models.SET_NULL, to='tasks.datedetail')),
                ('priority', models.OneToOneField(null=True, on_delete=models.SET_NULL, to='tasks.priority')),
                ('reported_by', models.ForeignKey(null=True, on_delete=models.SET_NULL, related_name='subtask_reported_by', to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(null=True, on_delete=models.SET_NULL, to='tasks.code')),
                ('tag', models.ForeignKey(null=True, on_delete=models.SET_NULL, to='tasks.tag')),
                ('task', models.ForeignKey(null=True, on_delete=models.SET_NULL, related_name='subs', to='tasks.task')),
                ('updated_by', models.ForeignKey(null=True, on_delete=models.SET_NULL, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectPhaseTemplateLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=models.SET_NULL, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL)),
                ('phase', models.ForeignKey(on_delete=models.CASCADE, to='tasks.phase')),
                ('project', models.ForeignKey(on_delete=models.CASCADE, to='tasks.project')),
                ('updated_by', models.ForeignKey(null=True, on_delete=models.SET_NULL, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectGroupLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=models.SET_NULL, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(on_delete=models.CASCADE, to='auth.group')),
                ('project', models.ForeignKey(on_delete=models.CASCADE, to='tasks.project')),
                ('updated_by', models.ForeignKey(null=True, on_delete=models.SET_NULL, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='phase',
            name='priority',
            field=models.OneToOneField(null=True, on_delete=models.SET_NULL, to='tasks.priority'),
        ),
        migrations.AddField(
            model_name='phase',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=models.SET_NULL, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('created_by', models.ForeignKey(null=True, on_delete=models.SET_NULL, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL)),
                ('date_detail', models.ForeignKey(null=True, on_delete=models.SET_NULL, to='tasks.datedetail')),
                ('phase', models.ForeignKey(null=True, on_delete=models.SET_NULL, to='tasks.phase')),
                ('updated_by', models.ForeignKey(null=True, on_delete=models.SET_NULL, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='grouptask',
            name='phase',
            field=models.ForeignKey(null=True, on_delete=models.SET_NULL, to='tasks.phase'),
        ),
        migrations.AddField(
            model_name='grouptask',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=models.SET_NULL, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL),
        ),
    ]
