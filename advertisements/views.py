from django.views.generic import DetailView,ListView
from .models import Advertisements




class DisplayAdvert(ListView):
    model = Advertisements
    context_object_name = 'advertisements'
    template_name = 'advertisements/advert_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['advertisements'] = context['advertisements'].filter(home_advert=True)
        return context


class AdvertDetails(DetailView):
    model = Advertisements
    context_object_name = 'advertisements'
    template_name = 'advertisements/advert_home_detail.html'

class DisplayHouseAdvert(ListView):
    model = Advertisements
    context_object_name = 'advertisements'
    template_name = 'advertisements/advert_house_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['advertisements'] = context['advertisements'].filter(house_advert=True)[0:3]
        return context




class DisplayFooterAdvert(ListView):
    model = Advertisements
    context_object_name = 'advertisements'
    template_name = 'advertisements/advert_footer_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['advertisements'] = context['advertisements'].filter(footer_advert=True)
        return context







