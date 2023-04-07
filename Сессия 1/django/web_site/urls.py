from django.urls import path
from .views import *

urlpatterns = [
    path('', LoginPageView.as_view(), name='index_page'),
    path('register/', RegisterView.as_view(), name='register_page'),
    path('home/', home, name='home_page'),
    path('request/', RequestView.as_view(), name='request_page'),
    path('g_request/', GroupRequestView.as_view(), name='g_request_page'),
]