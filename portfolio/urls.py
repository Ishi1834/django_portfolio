from django.urls import path
from .views import HomePageView, DocumentView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('resume/', DocumentView.as_view(), name='resume')
]