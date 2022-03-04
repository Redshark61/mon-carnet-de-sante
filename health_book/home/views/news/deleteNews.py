from django.views import View
from django.shortcuts import render, redirect
from login_signup.models.news import News
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

decorators = [
    permission_required('login_signup.can_use_medical_stuff', raise_exception=True),
    login_required(login_url='login')
]


@method_decorator(decorators, name='dispatch')
class DeleteNews(View):
    template_name = 'home/news/deleteNews.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        news = News.objects.get(pk=kwargs['pk'])
        news.delete()
        return redirect('home:newsList')
