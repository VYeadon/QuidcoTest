from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from coding_test.views import GIFRandomView, GIFSearchView

urlpatterns = [
    path('search', GIFSearchView.as_view(), name='gif_random'),
    path('random', GIFRandomView.as_view(), name='gif_search'),
]
