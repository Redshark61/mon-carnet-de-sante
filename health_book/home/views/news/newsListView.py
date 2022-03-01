from django.views.generic import ListView
from login_signup.models.news import News
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

decorators = [
    login_required(login_url='login')
]


@method_decorator(decorators, name='dispatch')
class NewsListView(ListView):
    model = News
    template_name = 'home/news/newsListView.html'
    context_object_name = 'news_list'
    paginate_by = 3
