<<<<<<< HEAD
=======
#
# # UserModel = get_user_model()
>>>>>>> origin/master
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model

<<<<<<< HEAD

=======
from _datetime import datetime
from django.http import request
# # Create your models here.
# UserModel = get_user_model()
#
#
>>>>>>> origin/master
class Mood(models.Model):
    VERY_LOW = 1
    LOW = 2
    NORMAL = 3
    HIGH = 4
    VERY_HIGH = 5

    mood_choices = (
        (VERY_LOW, 'Very Low'),
        (LOW, 'Low'),
        (NORMAL, 'Normal'),
        (HIGH, 'High'),
        (VERY_HIGH, 'Very High'),
    )
    mood = models.IntegerField(choices=mood_choices, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

<<<<<<< HEAD
    class Meta:
        ordering = ('-created_date',)
=======
    # def get_percentile(self):
    #     moods = Mood.objects.all()
    #     total_moods = sum([current_mood.mood for current_mood in moods])
    #     my_moods = sum(mood.rate for mood in moods if mood.created_by == self.created_by)
    #     return int(my_moods/total_moods)
    #
    # def get_date(self):
    #     date = Mood.objects.filter(created_by=self.created_by).first()
    #     return date.created_date

# # class MoodStat(models.Model):
# #     user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
# #
# #
# #     def get_percentile(self):
# #         moods = Mood.objects.all()
# #         total_moods = sum([mood.rate for mood in moods])
# #         my_moods = sum(mood.rate for mood in moods if mood.created_by == self.user)
# #         return int(my_moods/total_moods)
# #
# #     def get_streak(self):
# #         date = Mood.objects.filter(created_by=self.user).first()
# #         return date.created_date
#
# # class User(AbstractUser):
# #
# #     def get_percentile(self):
# #         moods = Mood.objects.all()
# #         total_moods = sum([mood.rate for mood in moods])
# #         my_moods = sum(mood.rate for mood in moods if mood.created_by == self.created_by)
# #         return int(my_moods/total_moods)
>>>>>>> origin/master
