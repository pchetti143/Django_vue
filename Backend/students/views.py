from students.serializers import StudentSerializer
from .models import students
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class StudentViewSet(ModelViewSet):
    queryset=students.objects.all()
    serializer_class=StudentSerializer
