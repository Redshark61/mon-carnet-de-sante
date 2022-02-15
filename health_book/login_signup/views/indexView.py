from django.views import View
from django.shortcuts import redirect, render


class IndexView(View):
    """
    Main page of the website
    """

    template_name = 'login_signup/index.html'

    @staticmethod
    def redirect_to_signup(request):
        """
        Redirect to the signup page dependig on the value of the button.
        The button value is like : `personal&login` or `personal&signup` or `medical&login` or `medical&signup`
        """

        person, direction = request.POST.get('button').split("&")

        if person == 'personal':
            response = redirect('login') if direction == 'login' else redirect('login_signup:signup', 1)
            response.set_cookie('medical', False)
            return response

        if person == 'medical':
            response = redirect('login') if direction == 'login' else redirect('login_signup:signup', 1)
            response.set_cookie('medical', True)
            return response

        return redirect('login_signup:index')

    def get(self, request):

        # Don't render immediately but first set the cookie
        response = render(request, self.template_name)
        response.set_cookie('medical', False)

        return response

    def post(self, request):
        resonse = self.redirect_to_signup(request)
        return resonse