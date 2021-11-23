from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields import DateTimeField, DurationField

from django.contrib.auth.models import User


class Department(models.Model):
    name = models.CharField(max_length=60, verbose_name="Название отдела")

    def __str__(self):
        return self.name


class Positions(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=60, verbose_name="Имя сотрудника")
    surname = models.CharField(max_length=60, verbose_name="Фамилия сотрудника")
    department = models.ForeignKey(Department, null=True, verbose_name="Отдел", on_delete=models.PROTECT)
    position = models.ForeignKey(Positions, on_delete=PROTECT, null=True,  verbose_name="Должность")
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    salary = models.IntegerField(verbose_name="Зарплата")

    def __str__(self):
        return self.name

    def _do_insert(self, manager, using, fields, returning_fields, raw):
        return super()._do_insert(manager, using, fields, returning_fields, raw)


class WorkCategory(models.Model):
    name = models.CharField(max_length=60, verbose_name="Категория работы")
    description = models.TextField(max_length=200, blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name


class WorkType(models.Model):
    name = models.CharField(max_length=100, verbose_name="Тип работы")
    description = models.TextField(max_length=200, blank=True, verbose_name="Описание")
    category = models.ForeignKey(WorkCategory, on_delete=PROTECT, verbose_name="Категория")

    def __str__(self):
        return self.name


class TimeLine(models.Model):
    start_at = DateTimeField()
    end_at = DateTimeField()
    total_work = DurationField()
    description = models.TextField(max_length=200, blank=True, verbose_name="Описание")
    employee = models.ForeignKey(Employee, on_delete=PROTECT)
    work_type = models.ManyToManyField(WorkType)

    def __str__(self):
        return '%s, %s' % (self.start_at, self.end_at)
