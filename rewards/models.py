from django.db import models
import datetime
from django.utils import timezone
from users.models import User

class Classification(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50) #分类名称：外卖，快递，跑腿，借雨伞,其他，等等

    def __str__(self):
        return self.name

# Create your models here.
class Reward(models.Model):
    id = models.IntegerField(primary_key=True)
    reward_title = models.CharField(max_length=100)#标题
    reward_text = models.CharField(max_length=200)#详细描述
    publisher = models.ForeignKey(User,on_delete=models.CASCADE,related_name='publisher') #user为父类，一个user对应多个rewards
    receiver = models.ForeignKey(User,on_delete=models.CASCADE,related_name='receiver')
    pub_date = models.DateTimeField('date published',default=timezone.now())
    prize = models.IntegerField(null=True) #价格
    position = models.CharField(max_length=200,null=True) #地点
    view_count = models.IntegerField(default=0) #浏览次数
    static_code = models.IntegerField(default=0) #状态码 0：未接单 1：已接单 2：已完成 3：申诉中 4：申诉成功 5：申诉失败
    classification = models.ForeignKey(Classification,on_delete=models.CASCADE,null=True) #分类为父类，一个分类可以对应个reward

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.reward_title

