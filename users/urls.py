from django.urls import path
from users import views

urlpatterns = [
    path('', views.login),
    path('/signup', views.signup),
    path('activate/<str:uid64>/<str:token>/', views.activate, name="activate"),
]
