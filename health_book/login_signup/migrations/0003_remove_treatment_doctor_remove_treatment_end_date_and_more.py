# Generated by Django 4.0.2 on 2022-02-02 09:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_signup', '0002_rename_doctor_id_appointment_doctor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treatment',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='treatment',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='treatment',
            name='is_permanent',
        ),
        migrations.RemoveField(
            model_name='treatment',
            name='prescription',
        ),
        migrations.RemoveField(
            model_name='treatment',
            name='user',
        ),
        migrations.AddField(
            model_name='customuser',
            name='treatments',
            field=models.ManyToManyField(related_name='User_treatment', to='login_signup.Treatment'),
        ),
        migrations.AddField(
            model_name='treatment',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='diseases',
            field=models.ManyToManyField(related_name='User_disease', through='login_signup.UserDisease', to='login_signup.Diseases'),
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescription', models.TextField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('is_permanent', models.BooleanField(default=False)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='login_signup.doctor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
