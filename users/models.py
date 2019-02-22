from django.db import models
from django.contrib.auth.models import AbstractUser
from mood.models import Mood
import datetime
from scipy.stats import percentileofscore
# from django.contrib.auth import get_user_model
# UserModel = get_user_model()
# Create your models here.

class CustomUser(AbstractUser):
    pass


    def get_current_streak(self):
        user_id = self.id
        mood_dates = [mood_date['created_date'] for mood_date in
                      Mood.objects.values('created_date').filter(created_by_id=user_id)]
        # date = datetime.date(mood_dates[1]['created_date']) - datetime.date(mood_dates[0]['created_date'])
        # print(date)
        current_streak = 0
        interval = 0
        today = datetime.date.today()
        next_date = today + datetime.timedelta(1)
        # for mood_date in mood_dates:
        #     mood_date = mood_date.date()
        #     interval = (next_date - mood_date).days
        #     if interval == 1:
        #         current_streak += 1
        #     elif interval == 0:
        #         pass
        #     else:
        #         break
        #     next_date = mood_date

        return mood_dates#(next_date-today).days

    def get_max_streak(self):
        user_id = self.id
        mood_dates = list(Mood.objects.values('created_date').filter(created_by_id=user_id).order_by('created_date'))
        # date = datetime.date(mood_dates[1]['created_date']) - datetime.date(mood_dates[0]['created_date'])
        # print(date)
        current_streak = 0
        max_streak = 0
        today = datetime.date.today()
        next_date = today + datetime.timedelta(1)
        for mood_date in mood_dates:
            mood_date = mood_date['created_date']
            interval = (next_date - mood_date.date()).days
            if  interval == 1:
                current_streak +=1
            elif interval == 0:
                pass
            else:
                max_streak = max(max_streak,current_streak)
                current_streak = 0   #reset streak
            max_streak = max(max_streak, current_streak)
            next_date = mood_date.date()

        return max_streak

    def get_max_streak_percentile(self):
        users = CustomUser.objects.all()
        all_max_streaks = [user.get_max_streak() for user in users]
        my_max_streak = self.get_max_streak()
        return percentileofscore(all_max_streaks,my_max_streak)


    # def get_percentile(self):
    #     moods = Mood.objects.all()
    #     total_moods = sum([mood.rate for mood in moods])
    #     my_moods = sum(mood.rate for mood in moods if mood.created_by == self.created_by)
