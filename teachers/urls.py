from django.urls import path,include
from . views import TeacherViewList,TeacherViewDetail

app_name = 'teachers'

urlpatterns = [
    path('',TeacherViewList.as_view(),name = 'teachers'),
    path('teacher/<int:pk>/',TeacherViewDetail.as_view(),name = 'teacher_detail'),
]