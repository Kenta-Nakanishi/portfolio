from django.db import models
from django.shortcuts import render
from requests import request


class indexModel(models.Model):
    title = models.CharField(verbose_name='タイトル', max_length=200)
    subtitle = models.CharField(verbose_name='サブタイトル', max_length=200)
    name = models.CharField(verbose_name='名前', max_length=200)
    introduction = models.TextField(verbose_name='紹介文')
    top_img = models.ImageField(verbose_name='トップ画像', upload_to='images')

    def __str__(self):
        return self.title


class customerModel(models.Model):
    name = models.CharField(verbose_name='名前', max_length=200)
    email = models.EmailField(verbose_name='メールアドレス',)
    content = models.TextField(verbose_name='本文')

    def __str__(self):
        return self.name