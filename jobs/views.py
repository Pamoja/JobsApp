from jobs.models import Job
from rest_framework import viewsets
from jobs.serializers import JobSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer