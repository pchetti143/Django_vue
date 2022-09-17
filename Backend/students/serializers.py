from rest_framework.serializers import ModelSerializer
from .models import students

class StudentSerializer(ModelSerializer):
    class Meta:
        model=students
        fields=['id','name','course','rating']