# Generated by Django 3.0.3 on 2020-04-06 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_user_githubtoken'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='github',
        ),
        migrations.AddField(
            model_name='user',
            name='github_username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]