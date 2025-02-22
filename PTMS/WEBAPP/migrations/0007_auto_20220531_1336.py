# Generated by Django 3.2.6 on 2022-05-31 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEBAPP', '0006_auto_20220530_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='EosemM',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='EosemMS',
            field=models.FileField(default='', upload_to='WEBAPP/files'),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='FisemM',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='FisemMS',
            field=models.FileField(default='', upload_to='WEBAPP/files'),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='SesemM',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='SesemMS',
            field=models.FileField(default='', upload_to='WEBAPP/files'),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='SisemM',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='SisemMS',
            field=models.FileField(default='', upload_to='WEBAPP/files'),
        ),
    ]
