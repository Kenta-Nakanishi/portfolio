# Generated by Django 3.2.9 on 2022-05-01 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortFolioApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='customerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='名前')),
                ('email', models.EmailField(max_length=254, verbose_name='メールアドレス')),
                ('content', models.TextField(verbose_name='本文')),
            ],
        ),
    ]
