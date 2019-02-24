from django.db import models
from django.contrib.auth.models import AbstractUser
from mood.models import Mood
import datetime
from scipy.stats import percentileofscore
# from django.contrib.auth import get_user_model
# UserModel = get_user_model()
# Create your models here.

<<<<<<< HEAD

class CustomUser(AbstractUser):
    pass

    def get_current_streak(self):
        '''
        Function to get current streak of the user.
        :return: current streak
        '''
        user_id = self.id
        mood_dates = [mood_date['created_date'] for mood_date in
                      Mood.objects.values('created_date').filter(created_by_id=user_id)]
=======
class CustomUser(AbstractUser):
    pass


    def get_current_streak(self):
        user_id = self.id
        mood_dates = list(Mood.objects.values('created_date').filter(created_by_id=user_id).order_by('created_date'))
        # date = datetime.date(mood_dates[1]['created_date']) - datetime.date(mood_dates[0]['created_date'])
        # print(date)
>>>>>>> origin/master
        current_streak = 0
        interval = 0
        today = datetime.date.today()
        next_date = today + datetime.timedelta(1)
        for mood_date in mood_dates:
<<<<<<< HEAD
            mood_date = mood_date.date()
            interval = (next_date - mood_date).days
            if interval == 1:
                current_streak += 1
=======
            mood_date = mood_date['created_date']
            interval = (next_date - mood_date.date()).days
            if  interval == 1:
                current_streak +=1
>>>>>>> origin/master
            elif interval == 0:
                pass
            else:
                break
<<<<<<< HEAD
            next_date = mood_date
        return current_streak

    def get_max_streak(self):
        '''
        Function to get max streak attained by the user.
        :return: max streak
        '''
        user_id = self.id
        mood_dates = [mood_date['created_date'] for mood_date in
                      Mood.objects.values('created_date').filter(created_by_id=user_id)]
        current_streak = 0
        interval = 0
=======
            next_date = mood_date.date()

        return current_streak

    def get_max_streak(self):
        user_id = self.id
        mood_dates = list(Mood.objects.values('created_date').filter(created_by_id=user_id).order_by('created_date'))
        # date = datetime.date(mood_dates[1]['created_date']) - datetime.date(mood_dates[0]['created_date'])
        # print(date)
        current_streak = 0
>>>>>>> origin/master
        max_streak = 0
        today = datetime.date.today()
        next_date = today + datetime.timedelta(1)
        for mood_date in mood_dates:
<<<<<<< HEAD
            mood_date = mood_date.date()
            interval = (next_date - mood_date).days
            if interval == 1:
                current_streak += 1
=======
            mood_date = mood_date['created_date']
            interval = (next_date - mood_date.date()).days
            if  interval == 1:
                current_streak +=1
>>>>>>> origin/master
            elif interval == 0:
                pass
            else:
                max_streak = max(max_streak,current_streak)
                current_streak = 0   #reset streak
            max_streak = max(max_streak, current_streak)
<<<<<<< HEAD
            next_date = mood_date
=======
            next_date = mood_date.date()
>>>>>>> origin/master

        return max_streak

    def get_max_streak_percentile(self):
<<<<<<< HEAD
        '''
        Function to compare user's max streak to other users and returns its percentile.
        :return:
        '''
=======
>>>>>>> origin/master
        users = CustomUser.objects.all()
        all_max_streaks = [user.get_max_streak() for user in users]
        my_max_streak = self.get_max_streak()
        return percentileofscore(all_max_streaks,my_max_streak)

<<<<<<< HEAD
=======

    # def get_percentile(self):
    #     moods = Mood.objects.all()
    #     total_moods = sum([mood.rate for mood in moods])
    #     my_moods = sum(mood.rate for mood in moods if mood.created_by == self.created_by)
>>>>>>> origin/master
