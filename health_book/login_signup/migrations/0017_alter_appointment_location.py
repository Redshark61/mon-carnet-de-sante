# Generated by Django 4.0.2 on 2022-02-15 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_signup', '0016_alter_customuser_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='location',
            field=models.CharField(default='9 rue de la source', max_length=100, verbose_name='Lieu'),
            preserve_default=False,
        ),
    ]
