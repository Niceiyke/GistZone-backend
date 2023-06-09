# Generated by Django 4.2 on 2023-04-07 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Profile_App', '0002_userprofile_blocked_userprofile_followers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='vote_ratio',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
