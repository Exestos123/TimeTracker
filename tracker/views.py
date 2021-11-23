from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.viewsets import ModelViewSet

from tracker.serializers import *


class UserModelViewSet(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    queryset = User.objects.all()
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    filter_fields = ['username', 'email']


class EmployeeModelViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    queryset = Employee.objects.all()
    filter_fields = ['name', 'surname', 'department', 'position']


class DepartmentModelViewSet(ModelViewSet):
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    queryset = Department.objects.all()
    filter_fields = ['name']


class PositionsModelViewSet(ModelViewSet):
    serializer_class = PositionsSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Positions.objects.all()
    filter_fields = ['name']


class WorkCategoryModelViewSet(ModelViewSet):
    serializer_class = WorkCategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = WorkCategory.objects.all()
    filter_fields = ['name']


class WorkTypeModelViewSet(ModelViewSet):
    serializer_class = WorkTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = WorkType.objects.all()
    filter_fields = ['name', 'category']


class TimeLineModelViewSet(ModelViewSet):
    serializer_class = TimeLineSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = TimeLine.objects.all()
    filter_fields = ['employee', 'work_type']
