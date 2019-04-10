from django.urls import path

from . import views

app_name = 'polls'#添加命名空间
#命名之后，就无需使用硬编码，想要修改url时，直接在本页面进行修改，在引用时引用的方式为"{% url 'detail' question.id %}"
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),





]