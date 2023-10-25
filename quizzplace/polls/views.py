from django.shortcuts import render
from rest_framework.views.generics import ListAPIView, get_object_or_404
from rest_framework.views import APIView
from .serializers import PollSerializer
from .models import Poll


class ActivePollsAPIView(ListAPIView):

    queryset = Poll.objects.filter(isActive=True)
    serializer_class = PollSerializer



class PollDetailAPIView(APIView):

    def get(self, poll_id):
        poll = get_object_or_404(Poll, pk=poll_id)
        serialized = PollSerializer(poll)
        return response(serialized.data)

    def post(self, poll_id):
        pass
