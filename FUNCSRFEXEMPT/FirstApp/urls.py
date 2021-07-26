from django.urls import path
from .views import *

urlpatterns=[
     path('employee/', employeelistview, name="Employeeview"),
    path('employee/<int:pk>/', employeedetailview)
    

]