# Generated by Django 4.0.2 on 2022-02-28 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_signup', '0041_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(choices=[('M', 'Message'), ('NP', 'New Patient')], default='M', max_length=10),
            preserve_default=False,
        ),
    ]
