from rest_framework import serializers

from .models import Student, Teacher, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('registration_date', 'last_login')

class StudentSerializer(UserSerializer):
    institution_id = serializers.PrimaryKeyRelatedField(read_only=True)
    subscription = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Student
        fields = ['user_name', 'password', 'first_name', 'last_name', 'email', 'registration_date', 'last_login', 'specialization', 'institution_id', 'subscription']
        read_only_fields = ('registration_date', 'last_login')

class TeacherSerializer(UserSerializer):
    institution_id = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Teacher
        fields = ['user_name', 'password', 'first_name', 'last_name', 'email', 'registration_date', 'last_login', 'specialization', 'institution_id']
        read_only_fields = ('registration_date', 'last_login')