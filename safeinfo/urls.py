from django.urls import path
from safeinfo    import views

urlpatterns = [
    path('/summary', views.summary),
    path('/cctv', views.cctv),
    path('/cctv_category', views.cctv_category),
]
