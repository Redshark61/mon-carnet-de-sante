from django.views import View
from django.shortcuts import redirect, render


class IndexView(View):
    template_name = 'login_signup/index.html'

    def render_to_response(self, context, **response_kwargs):
        response = super(IndexView, self).render_to_response(context, **response_kwargs)
        response.set_cookie('medical', False)
        return response

    def get(self, request):
        response = render(request, self.template_name)
        response.set_cookie('medical', False)

        return response

    def redirect_to_signup(self, request):
        person, direction = request.POST.get('button').split("&")
        print(person, direction)

        if person == 'personal':
            response = redirect('login') if direction == 'login' else redirect('login_signup:signup', 1)
            response.set_cookie('medical', False)
            return response

        if person == 'medical':
            response = redirect('login') if direction == 'login' else redirect(
                'login_signup:signup', 1)
            response.set_cookie('medical', True)
            return response

        return redirect('login_signup:index')

    def post(self, request):
        resonse = self.redirect_to_signup(request)
        return resonse
