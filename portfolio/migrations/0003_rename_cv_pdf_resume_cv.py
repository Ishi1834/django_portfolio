# Generated by Django 4.0.2 on 2022-02-24 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_resume'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume',
            old_name='cv_pdf',
            new_name='cv',
        ),
    ]
