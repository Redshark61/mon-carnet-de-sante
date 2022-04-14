from django.views.generic import CreateView
from login_signup.models.news import News
from django.urls import reverse_lazy
from home.forms import CreateNewsForm
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

decorators = [
    permission_required('login_signup.can_use_medical_stuff', raise_exception=True),
    login_required(login_url='login')
]


@method_decorator(decorators, name='dispatch')
class AddNews(CreateView):
    model = News
    form_class = CreateNewsForm
    template_name = 'home/news/addNews.html'
    success_url = reverse_lazy('home:newsList')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
