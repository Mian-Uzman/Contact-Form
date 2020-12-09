from . import views
from django.urls import path
urlpatterns = [
    path('submit/', views.form, name="form"),
]
