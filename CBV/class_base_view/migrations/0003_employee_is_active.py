# Generated by Django 3.2.18 on 2023-03-21 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_base_view', '0002_rename_emp_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
