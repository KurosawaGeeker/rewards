from django.shortcuts import render,get_list_or_404,get_object_or_404
from django.http import HttpResponse,JsonResponse
from .models import Reward
import json
from django.utils import timezone
from django.core.paginator import Paginator
# Create your rewards related views here.
def index(request):
    # if request.method == 'POST':
    #     try:
    #         data = json.loads(request.body)
    return('this is the index of rewards')


def detail(request,reward_id,):
    reward = get_object_or_404(Reward,pk=reward_id)
    #接受前端数据 需要测试
    id = request.raw_post
    print(id)
    print('测试数据')
    reward.view_count += 1#每次浏览 自动+1
    reward.save()
    data = dict()
    data['title'] = reward.reward_title
    data['text'] = reward.reward_text
    data['prize'] = reward.prize
    data['position'] = reward.positio
    data['publisher'] = reward.publisher.name
    data['tel'] = reward.publisher.tel
    data['view_count'] = reward.view_count
    data['static_code'] = reward.static_code
    data['pub_date'] = reward.pub_date
    return JsonResponse(data,json_dumps_params={'ensure_ascii':False})