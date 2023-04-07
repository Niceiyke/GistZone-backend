# Generated by Django 4.2 on 2023-04-07 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gist_App', '0005_remove_gistcomment_parent_alter_gist_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='gistcomment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Gist_App.gistcomment'),
        ),
        migrations.AlterField(
            model_name='gistcomment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
