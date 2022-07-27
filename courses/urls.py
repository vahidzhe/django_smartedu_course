from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.courses_list,name = 'courses'),
    path('<slug:category_slug>/<int:course_id>',views.course_detail,name = 'course_detail'),
    path('categories/<slug:category_slug>',views.courses_list,name = 'categoryses'),
    path('tags/<slug:tags_slug>',views.courses_list,name = 'tagses_list'),
    path('search>',views.search,name = 'search'),
  
]
