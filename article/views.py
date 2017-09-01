#from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from article.models import Article, Comments
# Create your views here.



def article_one(request):
	view = "article_one"
	html = "<html><body>THIS TEXT</body></html>"
	return HttpResponse(html)


def article_two(request):
	view = "article_two"
	return render_to_response('myview.html', {'name':view})	


def articles(request):
	return render_to_response('articles.html', {'articles':Article.objects.all()})


def article(request, id=1):
	return render_to_response('article.html', {'article': Article.objects.get(id=id), 'comments':Comments.objects.filter(comments_article_id=id)})
