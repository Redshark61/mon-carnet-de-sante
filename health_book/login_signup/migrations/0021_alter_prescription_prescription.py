# Generated by Django 4.0.2 on 2022-02-17 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_signup', '0020_appointment_is_active_alter_prescription_diseases_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='prescription',
            field=models.TextField(blank=True, null=True, verbose_name='Informations complémentaire'),
        ),
    ]
