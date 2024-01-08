from django.urls import path
from .views import (
    EmployeeApiView
)

urlpatterns = [
    path('employee/', EmployeeApiView.asview())
]