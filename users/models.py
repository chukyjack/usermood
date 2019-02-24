from django.db import models
from django.contrib.auth.models import AbstractUser
from mood.models import Mood
import datetime
from scipy.stats import percentileofscore



class CustomUser(AbstractUser):
    pass

    def get_current_streak(self):
        """
        Function to get current streak of the user.
        :return: current streak
        """
        user_id = self.id
        mood_dates = [mood_date['created_date'] for mood_date in
                      Mood.objects.values('created_date').filter(created_by_id=user_id)]
        current_streak = 0
        interval = 0
        today = datetime.date.today()
        next_date = today + datetime.timedelta(1)
        for mood_date in mood_dates:
            mood_date = mood_date.date()
            interval = (next_date - mood_date).days
            if interval == 1:
                current_streak += 1
            elif interval == 0:
                pass
            else:
                break
            next_date = mood_date
        return current_streak

    def get_max_streak(self):
        """
        Function to get max streak attained by the user.
        :return: max streak
        """
        user_id = self.id
        mood_dates = [mood_date['created_date'] for mood_date in
                      Mood.objects.values('created_date').filter(created_by_id=user_id)]
        current_streak = 0
        interval = 0
        max_streak = 0
        today = datetime.date.today()
        next_date = today + datetime.timedelta(1)
        for mood_date in mood_dates:
            mood_date = mood_date.date()
            interval = (next_date - mood_date).days
            if interval == 1:
                current_streak += 1
            elif interval == 0:
                pass
            else:
                max_streak = max(max_streak,current_streak)
                current_streak = 0   #reset streak
            max_streak = max(max_streak, current_streak)
            next_date = mood_date
        return max_streak

    def get_max_streak_percentile(self):
        '''
        Function to compare user's max streak to other users and returns its percentile.
        :return:
        '''
        users = CustomUser.objects.all()
        all_max_streaks = [user.get_max_streak() for user in users]
        my_max_streak = self.get_max_streak()
        return percentileofscore(all_max_streaks,my_max_streak)


