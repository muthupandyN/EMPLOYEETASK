# Generated by Django 3.2.9 on 2021-11-13 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmpTable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_name', models.CharField(max_length=200, null=True)),
                ('employee_email', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
