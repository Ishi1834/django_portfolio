# Generated by Django 4.0.2 on 2022-02-25 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_remove_resume_certificates'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='certificates',
            field=models.ManyToManyField(to='portfolio.Certificate'),
        ),
    ]