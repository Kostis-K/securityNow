from django.urls import path
from .views import (
    EmployeeApiView, StartView
)

urlpatterns = [
    path('hello', StartView.as_view()),
    path('employee', EmployeeApiView.as_view())
]