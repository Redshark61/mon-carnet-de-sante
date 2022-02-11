from django.views.generic.list import ListView
from login_signup.models.userDisease import UserDisease


class DiseasesView(ListView):
    model = UserDisease
    template_name = 'home/diseases.html'
    # context_object_name = 'disease_list'

    def get_queryset(self):
        queryset = super(DiseasesView, self).get_queryset()
        userDiseases = queryset.filter(user=self.request.user)
        # # print(userDiseases.get(username=self.request.user))
        print(userDiseases)
        return userDiseases
