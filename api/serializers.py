from rest_framework import serializers
from mood.models import Mood
import datetime


class MoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mood
        fields = ('mood',)

    def create(self, data):
        '''
        Function overides the create method of base class ModelSerializer so we include
        the created date and created user for each mood POSTed.
        :param data: posted data
        :return:
        '''
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        data['created_date'] = datetime.date
        data['created_by'] = user
        # data['percentile'] = user
        # data['streak'] = user
        return super().create(data)

