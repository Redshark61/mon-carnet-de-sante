from django.views import View
from django.shortcuts import render, redirect
from login_signup.models.news import News


class DeleteNews(View):
    template_name = 'home/news/deleteNews.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        news = News.objects.get(pk=kwargs['pk'])
        news.delete()
        return redirect('home:newsList')
