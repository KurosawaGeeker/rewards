from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class User(models.Model):
    openid = models.CharField(max_length=200) #微信账户的openid
    session_key = models.CharField(max_length=200) #微信账户的session_key 以此以上两项来作为微信端用户的登录凭证 从wx.login()和wx.request()获取
    name = models.CharField(max_length=50)#用户的真实姓名
    school = models.CharField(max_length=200)
    tel = models.CharField(max_length=50)
    QQ = models.CharField(max_length=50)
    authenticated = models.BooleanField()#是否已经通过实名认证，此项由人工确认
    card = models.ImageField(upload_to='img')#上传校园卡照片






