# Generated by Django 3.1 on 2020-08-09 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PiiData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cc_number', models.CharField(max_length=200)),
                ('cc_exp', models.CharField(max_length=200)),
                ('cc_cvv', models.CharField(max_length=200)),
            ],
        ),
    ]
