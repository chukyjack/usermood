from rest_framework import serializers
from mood.models import Mood
<<<<<<< HEAD
import datetime


class MoodSerializer(serializers.ModelSerializer):

=======
from django.contrib.auth import get_user_model
import datetime
from collections import OrderedDict


# class MoodStatSerializer(serializers.ModelSerializer):
#     percentile = serializers.CharField(source='get_percentile', read_only=True)
#     streak = serializers.CharField()
#     class Meta:
#         model = MoodStat
#         fields = ('percentile',)
#
#     # def to_representation(self, instance):
#     #     result = super(MoodSerializer, self).to_representation(instance)
#     #     return OrderedDict([(key, result[key]) for key in result if not (key == 'percentiles' and result[key]  > 19)])


class MoodSerializer(serializers.ModelSerializer):
    # percentile = serializers.CharField(source='get_percentile', read_only=True)
    # final = serializers.CharField()
    # moodstat = MoodStatSerializer(many=True,read_only=True)
>>>>>>> origin/master
    class Meta:
        model = Mood
        fields = ('mood',)

<<<<<<< HEAD
    def create(self, data):
        '''
        Function overides the create method of base class ModelSerializer so we include
        the created date and created user for each mood POSTed.
        :param data: posted data
        :return:
        '''
=======
    # def to_representation(self, instance):
    #     result = super(MoodSerializer, self).to_repraesentation(instance)
    #     return OrderedDict([(key, result[key]) for key in result if not (key == 'percentiles' and result[key]  > 19)])

    def create(self, data):
        # Will only be done if a new object is being created
>>>>>>> origin/master
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        data['created_date'] = datetime.date
        data['created_by'] = user
        # data['percentile'] = user
        # data['streak'] = user
        return super().create(data)

