from jobs.models import Job
from rest_framework import serializers

class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = ('id', 'title', 'description', 'location', 'company', 'email', 'created_at')