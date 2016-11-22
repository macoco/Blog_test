from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article   #要记得导入文章这个类才行，找不到name就找这里~
from datetime import datetime


# Create your views here.
def home(request):
    return HttpResponse("Hello World, Django")

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

'''
def detail(request, my_args):
        post = Article.objects.all()[int(my_args)]  #通过参数访问数据库资源
        str = ("title = %s, category = %s, date_time = %s, content = %s" % (post.title, post.category, post.date_time, post.content))
        return HttpResponse(str)
'''

#模板要放在子目录下，然后写上路径。
def home(request):
    post_list = Article.objects.all()  #获取全部的Article对象
    return render(request, 'article/home.html', {'post_list' : post_list})

def detail(request, id):
        try:
            post = Article.objects.get(id=str(id))   #get可以取得每一篇文章的id
        except Article.DoesNotExist:
            raise Http404
        return render(request, 'article/post.html', {'post' : post})


'''
def test(request) :
    return render(request, 'article/test.html', {'current_time': datetime.now()})
  '''  
