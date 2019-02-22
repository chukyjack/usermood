from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
# from datetime import datetime
import datetime
from . import serializers
from mood.models import Mood
from api.serializers import MoodSerializer



# @api_view(['GET', 'POST'])
# def mood_list(request):
#     """
#     List all moods created by user, or submit new mood.
#     """
#     if request.method == 'GET':
#         moods = Mood.objects.filter(created_by=request.user)
#         user = request.user
#         moods = user.mood_set.all()
#         percentile = 0
#         for mood in moods:
#             percentile += mood.rate
#         percentile = percentile / 100
#         serializer = MoodSerializer(moods, context= {'percentile':percentile}, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = MoodSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(
#                 serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
class ListMood(generics.ListCreateAPIView):
    queryset = Mood.objects.all()
    serializer_class = MoodSerializer

    def get_queryset(self):
        user = self.request.user
        return user.mood_set.all()

    # def get_current_streak(self):
    #     user = self.request.user
    #     mood_dates = list(Mood.objects.values('created_date').filter(created_by=user).order_by('created_date'))
    #     # date = datetime.date(mood_dates[1]['created_date']) - datetime.date(mood_dates[0]['created_date'])
    #     # print(date)
    #     current_streak = 0
    #     interval = 0
    #     today = datetime.date.today()
    #     next_date = today + datetime.timedelta(1)
    #     for mood_date in mood_dates:
    #         mood_date = mood_date['created_date']
    #         interval = (next_date - mood_date.date()).days
    #         if  interval == 1:
    #             current_streak +=1
    #         elif interval == 0:
    #             pass
    #         else:
    #             break
    #         next_date = mood_date.date()
    #
    #     return current_streak #datetime.date(mood_date)
    #
    # def get_max_streak(self):
    #     user = self.request.user
    #     mood_dates = list(Mood.objects.values('created_date').filter(created_by=user).order_by('created_date'))
    #     # date = datetime.date(mood_dates[1]['created_date']) - datetime.date(mood_dates[0]['created_date'])
    #     # print(date)
    #     current_streak = 0
    #     max_streak = 0
    #     today = datetime.date.today()
    #     next_date = today + datetime.timedelta(1)
    #     for mood_date in mood_dates:
    #         mood_date = mood_date['created_date']
    #         interval = (next_date - mood_date.date()).days
    #         if  interval == 1:
    #             current_streak +=1
    #         elif interval == 0:
    #             pass
    #         else:
    #             max_streak = max(max_streak,current_streak)
    #             current_streak = 0   #reset streak
    #         max_streak = max(max_streak, current_streak)
    #         next_date = mood_date.date()
    #
    #     return max_streak
    #
    # def get_max_streak_percentile(self):
    #     users = UserModel.objects.all()
    #
    #     pass

    def list(self, request, *args, **kwargs):
        response = super().list(request, args, kwargs)
        # Add data to response.data Example for your object:
        user = self.request.user
        moods = user.mood_set.all()
        mood_stat = [{'Current streak': user.get_current_streak()},
                     {'Maximum streak percentile': user.get_max_streak_percentile()}]
        response.data = mood_stat + response.data # Or wherever you get this values from
        return response

    # def get_serializer_context(self):
    #     context = super().get_serializer_context()
    #     context['foo'] = 'bar'
    #     return context
