from django.shortcuts import render,get_list_or_404,get_object_or_404
from django.http import HttpResponse
from users.models import User
from rewards.models import Reward
# Create your user related views here.
def index(request):
    return HttpResponse("Hello, world. You're at the users index.")

def myself(request,user_id):
    myself = get_object_or_404(User,pk=user_id)
    p_reward = Reward.objects.filter(publisher_id=user_id)
    r_reward = Reward.objects.filter(receiver_id=user_id)
    p_count = p_reward.count()#输出接单的数量
    r_count = r_reward.count()
    tel = myself.tel
    school = myself.school
    authenticated = myself.authenticated



    data = dict()
    data['p_count']


