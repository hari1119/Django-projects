# Generated by Django 3.2.19 on 2023-06-08 06:31

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('mobile_number', models.CharField(max_length=13, verbose_name='Mobile Number')),
                ('date_of_birth', models.DateField(verbose_name='D.O.B')),
                ('bloog_group', models.CharField(max_length=5, verbose_name='Blood Group')),
                ('gender', models.CharField(max_length=10, verbose_name='Gender')),
                ('whatspp_number', models.CharField(max_length=13, verbose_name='Whatsapp Number')),
                ('address_line_1', models.TextField(max_length=100, verbose_name='Address Line 1')),
                ('address_line_2', models.TextField(blank=True, max_length=100, null=True, verbose_name='Address Line 2')),
                ('city', models.CharField(max_length=50, verbose_name='City')),
                ('state', models.CharField(max_length=50, verbose_name='state')),
                ('postal_code', models.CharField(max_length=10, verbose_name='Postal code')),
                ('father_name', models.CharField(max_length=50, verbose_name='Father Name')),
                ('mother_name', models.CharField(max_length=50, verbose_name='Mother Name')),
                ('martial_statue', models.CharField(blank=True, max_length=10, null=True, verbose_name='Martial Status')),
                ('wife_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Wife Name')),
                ('language', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20, verbose_name='Languages'), size=None)),
                ('sports', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Spors'), size=None)),
                ('hobby', models.CharField(blank=True, max_length=100, null=True, verbose_name='Hobbies')),
                ('current_company', models.CharField(max_length=100, verbose_name='Current company')),
                ('current_company_location', models.CharField(max_length=150, verbose_name='Current company location')),
                ('previous_company', models.CharField(blank=True, max_length=100, null=True, verbose_name='Previous company')),
                ('previous_company_location', models.CharField(blank=True, max_length=150, null=True, verbose_name='Previous company location')),
                ('designation', models.CharField(max_length=50, null=True, verbose_name='Designation')),
                ('year_of_experience', models.CharField(max_length=10, verbose_name='Years of Experience')),
            ],
            options={
                'verbose_name_plural': 'Employee Details',
                'db_table': 'employee_details',
            },
        ),
    ]
