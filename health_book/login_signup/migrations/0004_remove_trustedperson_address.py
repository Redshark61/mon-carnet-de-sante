# Generated by Django 4.0.2 on 2022-02-02 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_signup', '0003_remove_treatment_doctor_remove_treatment_end_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trustedperson',
            name='address',
        ),
    ]
