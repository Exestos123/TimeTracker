from rest_framework import serializers
from tracker.models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ('id', 'name', )


class PositionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Positions
        fields = ('id', 'name', )


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('id', 'name', 'surname', 'department', 'position', 'user', 'salary', )


class WorkCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkCategory
        fields = ('id', 'name', 'description', )


class WorkTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkType
        fields = ('id', 'name', 'description', 'category', )


class TimeLineSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimeLine
        fields = ('id', 'start_at', 'end_at', 'total_work', 'description', 'employee', 'work_type', )
