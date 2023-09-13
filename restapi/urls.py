from django.urls import path
from .views import PersonView


urlpatterns = [
    path('user_id/', PersonView.as_view()),
    path('user_id/<int:id>', PersonView.as_view()),
]