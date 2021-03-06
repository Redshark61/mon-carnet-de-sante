# Generated by Django 4.0.2 on 2022-02-24 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_signup', '0035_alter_customuser_blocked_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='blocked_user',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='main_doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='User_main_doctor', to='login_signup.doctor'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='treatments',
            field=models.ManyToManyField(blank=True, null=True, related_name='User_treatment', to='login_signup.Treatment'),
        ),
    ]
