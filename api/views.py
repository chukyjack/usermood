from rest_framework import generics
from mood.models import Mood
from api.serializers import MoodSerializer


class ListMood(generics.ListCreateAPIView):
    queryset = Mood.objects.all()
    serializer_class = MoodSerializer

    def get_queryset(self):
        '''
        Function to overide GET method of base class and returns only post made by
        the user.
        :return:
        '''
        user = self.request.user
        return user.mood_set.all()

    def list(self, request, *args, **kwargs):
        '''
        Function that overwrites the list method of Base class LIstCreateAPIView
        and include extra data to our json response body.
        :param request:
        :param args:
        :param kwargs:
        :return: response
        '''
        response = super().list(request, args, kwargs)
        user = self.request.user
        max_streak_percentile = user.get_max_streak_percentile()
        mood_stat = [{'Current streak': user.get_current_streak()}]
        if max_streak_percentile >= 50:
            mood_stat.append({'Maximum streak percentile': int(user.get_max_streak_percentile())})
        response.data = mood_stat + response.data
        return response
