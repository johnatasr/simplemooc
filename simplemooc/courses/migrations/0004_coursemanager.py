# Generated by Django 2.1.2 on 2018-11-29 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20181129_0853'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
