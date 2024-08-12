# Generated by Django 3.2.6 on 2022-05-31 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEBAPP', '0008_auto_20220531_1443'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='Job_ID',
            new_name='ComAdd',
        ),
        migrations.AddField(
            model_name='company',
            name='ComPort',
            field=models.FileField(default='', null=True, upload_to='WEBAPP/files'),
        ),
        migrations.AddField(
            model_name='company',
            name='CompanyId',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='company',
            name='FromFilld',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='company',
            name='Cmnyimage',
            field=models.ImageField(default='', null=True, upload_to='FASHION/images'),
        ),
    ]
