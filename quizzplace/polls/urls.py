from django.urls import path
from .views import ActivePollsAPIView


app_name = "poll"


urlpatterns = [
    path("polls/", ActivePollsAPIView.as_view(), name="active_polls"),

]