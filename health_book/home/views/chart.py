from django.views.generic import TemplateView


class ChartView(TemplateView):
    template_name = 'home/chart.html'
