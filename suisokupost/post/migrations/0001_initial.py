# Generated by Django 3.1.3 on 2021-02-28 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('user_name', models.CharField(max_length=200, null=True)),
                ('day_now', models.CharField(max_length=20, null=True)),
                ('time_now', models.CharField(max_length=20, null=True)),
                ('time_hours', models.CharField(max_length=20, null=True)),
                ('time_minutes', models.CharField(max_length=20, null=True)),
                ('time_seconds', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
