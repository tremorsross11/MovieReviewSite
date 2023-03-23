from . import views
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', views.MoviePicker_home, name='MoviePicker_home'),
    path('generate/', views.MoviePicker_generate, name='MoviePicker_generate'),
    path('view/', views.MoviePicker_view, name='MoviePicker_view'),
    path('<int:pk>/details/', views.MoviePicker_details, name='MoviePicker_details'),
    path('<int:pk>/delete/', views.delete, name='MoviePicker_delete'),
    path('<int:pk>/update/', views.update, name='MoviePicker_update'),
    path('bs/', views.MoviePicker_bs, name='MoviePicker_bs')

]