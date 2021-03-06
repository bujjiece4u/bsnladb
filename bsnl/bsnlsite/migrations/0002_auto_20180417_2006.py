# Generated by Django 2.0.4 on 2018-04-17 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bsnlsite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bsnlsitedb',
            name='ac',
        ),
        migrations.AddField(
            model_name='bsnlsitedb',
            name='ac1capacity',
            field=models.CharField(choices=[('1t', '1T'), ('1.5t', '1.5T'), ('2t', '2T'), ('2.5t', '2.5T')], default='1T', max_length=4),
        ),
        migrations.AddField(
            model_name='bsnlsitedb',
            name='ac2capacity',
            field=models.CharField(choices=[('1t', '1T'), ('1.5t', '1.5T'), ('2t', '2T'), ('2.5t', '2.5T')], default='1T', max_length=4),
        ),
        migrations.AddField(
            model_name='bsnlsitedb',
            name='ac3capacity',
            field=models.CharField(choices=[('1t', '1T'), ('1.5t', '1.5T'), ('2t', '2T'), ('2.5t', '2.5T')], default='1T', max_length=4),
        ),
        migrations.AddField(
            model_name='bsnlsitedb',
            name='ac4capacity',
            field=models.CharField(choices=[('1t', '1T'), ('1.5t', '1.5T'), ('2t', '2T'), ('2.5t', '2.5T')], default='1T', max_length=4),
        ),
        migrations.AddField(
            model_name='bsnlsitedb',
            name='ac5capacity',
            field=models.CharField(choices=[('1t', '1T'), ('1.5t', '1.5T'), ('2t', '2T'), ('2.5t', '2.5T')], default='1T', max_length=4),
        ),
        migrations.AddField(
            model_name='bsnlsitedb',
            name='powerplantmodule',
            field=models.CharField(choices=[('50a', '50A'), ('10a', '10A'), ('25a', '25A'), ('100a', '100A')], default='50A', max_length=4),
        ),
        migrations.AlterField(
            model_name='bsnlsitedb',
            name='battery',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='bsnlsitedb',
            name='btstype',
            field=models.CharField(choices=[('2g', '2G'), ('3g', '3G'), ('2g+3g', '2G+3G'), ('te', 'TE'), ('te+2g', 'TE+2G'), ('te+2g+3g', 'TE+2G+3G')], default='2G', max_length=8),
        ),
        migrations.AlterField(
            model_name='bsnlsitedb',
            name='powerplant',
            field=models.CharField(max_length=200),
        ),
    ]
