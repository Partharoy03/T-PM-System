# Generated by Django 3.2.6 on 2022-06-15 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEBAPP', '0014_studentprofile_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='AppDt',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='StatusJ',
            field=models.TextField(null=True),
        ),
    ]
