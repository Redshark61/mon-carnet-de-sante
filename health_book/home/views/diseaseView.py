from django.views.generic.list import ListView
from login_signup.models.userDisease import UserDisease


class DiseasesView(ListView):
    model = UserDisease
    template_name = 'home/diseases.html'

    def get_queryset(self):
        """
        Display the diseases for the current user
        """
        queryset = super(DiseasesView, self).get_queryset()
        userDiseases = queryset.filter(user=self.request.user)
        print(userDiseases)
        return userDiseases
