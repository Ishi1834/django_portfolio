# Generated by Django 4.0.2 on 2022-02-25 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_rename_certificates_certificate'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='certificates',
            field=models.ManyToManyField(to='portfolio.Certificate'),
        ),
    ]
