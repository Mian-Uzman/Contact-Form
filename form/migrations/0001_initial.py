# Generated by Django 3.1.3 on 2020-12-09 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.IntegerField(max_length=15)),
                ('email', models.EmailField(max_length=200)),
                ('comments', models.CharField(max_length=500)),
            ],
        ),
    ]
