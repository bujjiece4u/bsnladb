# Generated by Django 2.0.4 on 2018-04-17 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bsnlsite', '0002_auto_20180417_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='bsnlsitedb',
            name='ac1make',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bsnlsitedb',
            name='ac2make',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bsnlsitedb',
            name='ac3make',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bsnlsitedb',
            name='ac4make',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bsnlsitedb',
            name='ac5make',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bsnlsitedb',
            name='batterytype',
            field=models.CharField(choices=[('100ah', '100AH'), ('200ah', '200AH'), ('300ah', '300AH')], default='100AH', max_length=5),
        ),
    ]