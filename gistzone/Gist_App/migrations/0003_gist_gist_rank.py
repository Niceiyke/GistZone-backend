# Generated by Django 4.2 on 2023-04-04 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gist_App', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gist',
            name='gist_rank',
            field=models.PositiveIntegerField(default=0),
        ),
    ]