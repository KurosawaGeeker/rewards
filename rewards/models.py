from django.db import models
import datetime
from django.utils import timezone
from users.models import User


# Create your models here.
class Reward(models.Model):
    reward_title = models.CharField(max_length=100)
    reward_text = models.CharField(max_length=200)
    publisher = models.ForeignKey(User,on_delete=models.CASCADE,related_name='publisher') #user为父类，一个user对应多个rewards
    receiver = models.ManyToManyField(User,related_name='receiver')
    # pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.reward_title

