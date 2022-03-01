from django.views.generic import ListView
from login_signup.models.news import News


class NewsListView(ListView):
    model = News
    template_name = 'home/news/newsListView.html'
    context_object_name = 'news_list'
    paginate_by = 3
