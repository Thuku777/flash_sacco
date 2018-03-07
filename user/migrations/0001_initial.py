# Generated by Django 2.0.2 on 2018-03-04 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupAccName', models.CharField(max_length=100)),
                ('groupAccNo', models.IntegerField()),
                ('groupAccBal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_date', models.DateField(auto_now=True)),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('IDnumber', models.IntegerField()),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('DateOfBirth', models.DateField()),
                ('address', models.CharField(max_length=50)),
                ('code', models.IntegerField()),
                ('town', models.CharField(max_length=30)),
                ('accountPin', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20)),
                ('marital', models.CharField(choices=[('single', 'single'), ('married', 'married')], max_length=10)),
                ('employed', models.BooleanField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]