from django.db import models
from django.contrib.auth import hashers
# Create your models here.


class User(models.Model):

    username = models.CharField(verbose_name="用户名", max_length=100)
    password = models.CharField(verbose_name="密码", max_length=100)
    age = models.PositiveSmallIntegerField(verbose_name="年龄")
    createtime = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    modifytime = models.DateTimeField(verbose_name="修改时间", auto_now=True)

    def __str__(self):
        return self.username

    def hash_password(self, val):
        return hashers.make_password(val)

    def check_password(self, password):
        if hashers.check_password(password, self.password):
            return True
        else:
            return False


class Book(models.Model):

    name = models.CharField(verbose_name="书名", max_length=100)
    user = models.ManyToManyField("User")
    createtime = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    modifytime = models.DateTimeField(verbose_name="修改时间", auto_now=True)
