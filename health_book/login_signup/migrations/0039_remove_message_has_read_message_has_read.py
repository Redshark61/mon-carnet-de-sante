# Generated by Django 4.0.2 on 2022-02-24 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_signup', '0038_remove_message_is_read_message_has_read'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='has_read',
        ),
        migrations.AddField(
            model_name='message',
            name='has_read',
            field=models.BooleanField(default=False),
        ),
    ]
