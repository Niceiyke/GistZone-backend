# Generated by Django 4.2 on 2023-04-07 14:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Gist_App', '0003_gist_gist_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gist',
            name='title',
            field=models.CharField(max_length=500),
        ),
        migrations.CreateModel(
            name='GistComment',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name=uuid.uuid4)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Gist_App.gist')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Gist_App.gistcomment')),
            ],
        ),
    ]