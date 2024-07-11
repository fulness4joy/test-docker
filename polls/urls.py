from django.urls import path
from .views import *


urlpatterns = [
    path('', PollsList.as_view(), name="index"),
    path('detail/<int:pk>', PollDetail.as_view(), name="poll-detail"),
    path('create/', PollCreate.as_view(), name='poll-create'),
    path('ajax-test', AjaxTestView.as_view(), name="ajax-test"),
    path('ajax-request', ajax_request, name="ajax-request"),
]