# Generated by Django 4.0.2 on 2022-02-28 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_signup', '0042_notification_notification_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='content',
            field=models.CharField(max_length=100, null=True),
        ),
    ]