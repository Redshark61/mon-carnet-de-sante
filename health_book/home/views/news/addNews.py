from django.views.generic import CreateView
from login_signup.models.news import News
from django.urls import reverse_lazy
from home.forms import CreateNewsForm


class AddNews(CreateView):
    model = News
    form_class = CreateNewsForm
    template_name = 'home/news/addNews.html'
    success_url = reverse_lazy('home:news_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
