# Generated by Django 3.2.20 on 2023-09-29 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landrecords', '0003_rename_name_logindata_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='newEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('fname', models.CharField(default='', max_length=50)),
                ('state', models.CharField(default='', max_length=50)),
                ('district', models.CharField(default='', max_length=50)),
                ('city', models.CharField(default='', max_length=50)),
                ('pincode', models.CharField(max_length=10)),
            ],
        ),
    ]