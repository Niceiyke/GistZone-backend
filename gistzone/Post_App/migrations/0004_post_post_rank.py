# Generated by Django 4.2 on 2023-04-04 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post_App', '0003_alter_downvote_downvoter_alter_upvote_upvoter'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_rank',
            field=models.PositiveIntegerField(default=0),
        ),
    ]