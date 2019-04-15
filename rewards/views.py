from django.shortcuts import render,get_list_or_404,get_object_or_404
from django.http import HttpResponse
from .models import Reward
from django.utils import timezone
# Create your rewards related views here.
def index(request):
    return HttpResponse("Hello, world. You're at the rewards index.")

def detail(request,reward_id):
    reward = get_object_or_404(Reward,pk=reward_id)
    return render(request,'polls/detail.html',{'reward':reward})