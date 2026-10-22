
from django.contrib import admin
from django.urls import path
from studentapp.views import addStudent, viewStudent, updateStudent, fetchStudent, deleteStudent

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/addstudents/', addStudent),
    path('api/viewstudent/', viewStudent),
    path('api/updatestudent/<int:id>/', updateStudent),
    path('api/fetchstudent/<int:id>/', fetchStudent),
    path('api/deletestudent/<int:id>/', deleteStudent),
]
