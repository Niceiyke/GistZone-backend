# Generated by Django 4.2 on 2023-04-09 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gist_App', '0008_category_gist_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
