# Generated by Django 4.2 on 2023-04-04 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Gist_App', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='upvote',
            name='upvoter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gist_upvoter', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='image',
            name='gist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Gist_App.gist'),
        ),
        migrations.AddField(
            model_name='gist',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='downvote',
            name='downvoter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gist_downvoter', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='downvote',
            name='gist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='downvotes', to='Gist_App.gist'),
        ),
    ]
