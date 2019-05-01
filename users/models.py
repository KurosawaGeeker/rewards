from django.db import models
import datetime
from django.utils import timezone

# Create your models here.


class School(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)  #学校名

class Campus(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200) #校区名
    school = models.ForeignKey(School,on_delete=models.CASCADE)

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    openid = models.CharField(max_length=100, blank=True, null=True, verbose_name="openid", unique=True)
    session_key = models.CharField(max_length=200) #微信账户的session_key 以此以上两项来作为微信端用户的登录凭证 从wx.login()和wx.request()获取
    username = models.CharField(max_length=200) #用户名，自行设置
    name = models.CharField(max_length=50)#用户的真实姓名
    schoolo = models.ForeignKey(School,on_delete=models.CASCADE,null=True)
    campus = models.ForeignKey(Campus,on_delete=models.CASCADE,null=True)
    tel = models.CharField(max_length=50)
    QQ = models.CharField(max_length=50)
    authenticated = models.BooleanField()#是否已经通过实名认证，此项由人工确认
    card = models.ImageField(upload_to='img')#上传校园卡照片









