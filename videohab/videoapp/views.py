from django.shortcuts import render
from django.db.models import Q
from django.views.generic import TemplateView, ListView

from .models import Clips


class HomePageView(TemplateView):
    template_name = 'home.html'


class SearchResultsView(ListView):
    model = Clips
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Clips.objects.filter(
            Q(clips_name__icontains=query) | Q(clips_comment__icontains=query) | Q(clips_hashtag__icontains=query)
        )
        return object_list

