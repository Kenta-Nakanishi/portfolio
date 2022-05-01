# Generated by Django 3.2.9 on 2022-04-30 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='indexModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='タイトル')),
                ('subtitle', models.CharField(max_length=200, verbose_name='サブタイトル')),
                ('name', models.CharField(max_length=200, verbose_name='名前')),
                ('introduction', models.TextField(verbose_name='紹介文')),
                ('top_img', models.ImageField(upload_to='images', verbose_name='トップ画像')),
            ],
        ),
    ]