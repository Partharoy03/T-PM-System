# Generated by Django 3.2.6 on 2022-05-31 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEBAPP', '0007_auto_20220531_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='EosemMS',
            field=models.FileField(default='', null=True, upload_to='WEBAPP/files'),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='FisemMS',
            field=models.FileField(default='', null=True, upload_to='WEBAPP/files'),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='FosemMS',
            field=models.FileField(default='', null=True, upload_to='WEBAPP/files'),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='SesemMS',
            field=models.FileField(default='', null=True, upload_to='WEBAPP/files'),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='SisemMS',
            field=models.FileField(default='', null=True, upload_to='WEBAPP/files'),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='SsemMS',
            field=models.FileField(default='', null=True, upload_to='WEBAPP/files'),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='TsemMS',
            field=models.FileField(default='', null=True, upload_to='WEBAPP/files'),
        ),
    ]