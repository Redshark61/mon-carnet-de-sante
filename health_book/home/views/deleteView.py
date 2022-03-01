from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

decorators = [
    login_required(login_url='login')
]


@method_decorator(decorators, name='dispatch')
class DeleteView(View):
    """
    View to delete the user
    """
    template_name = 'home/delete.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        """
        Delete the user
        """
        if request.POST.get('button') == 'delete':
            request.user.delete()
            return redirect('index')
        else:
            return redirect('home:settings')
