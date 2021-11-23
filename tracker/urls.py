from django.urls import path, include
from rest_framework.routers import SimpleRouter

from tracker import admin
from tracker.views import *

router = SimpleRouter()

router.register(r'user', UserModelViewSet)
router.register(r'employee', EmployeeModelViewSet)
router.register(r'department', DepartmentModelViewSet)
router.register(r'positions', PositionsModelViewSet)
router.register(r'workcategory', WorkCategoryModelViewSet)
router.register(r'worktype', WorkTypeModelViewSet)
router.register(r'timeline', TimeLineModelViewSet)

urlpatterns = router.urls
