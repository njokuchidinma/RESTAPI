from django.urls import path
from .views import CreatePersonView ,PersonView, NameView


urlpatterns = [
    path('',CreatePersonView.as_view()),
    path('<int:id>', PersonView.as_view()),
    path('<str:nameid>', NameView.as_view()),
]