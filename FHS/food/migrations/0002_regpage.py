# Generated by Django 4.1.7 on 2023-03-23 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='regpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.EmailField(max_length=254)),
                ('mail', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=10)),
                ('phno', models.TextField()),
            ],
        ),
    ]
