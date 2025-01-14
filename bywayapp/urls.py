from django.urls import path
from.import views


app_name = "bywayapp"  # Add this line

urlpatterns = [
    path('',views.home,name='home'),
    path('singlepage/<int:pk>', views.pageRoute, name='singlepage'),
    path('coursespage/', views.listCourses, name='coursespage'),
    path('listCourses/',views.listCourses, name='listCourses'),
    path('ViewCategory/<int:pk>',views.ViewCategory,name='ViewCategory'),
]