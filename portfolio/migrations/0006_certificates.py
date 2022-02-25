# Generated by Django 4.0.2 on 2022-02-25 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_alter_project_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('website', models.URLField(blank=True, null=True)),
                ('issued_on', models.DateField()),
                ('organisation', models.CharField(max_length=200)),
                ('tech_stack', models.ManyToManyField(to='portfolio.TechStack')),
            ],
            options={
                'ordering': ['-issued_on'],
            },
        ),
    ]