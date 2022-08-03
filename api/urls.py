from django.urls import path
from .views import TodoListView, TodoListViewCreate, TodoRetrieveUpdateDestroy, TodoToggleComplete, signup, login


urlpatterns=[
    path('todos/', TodoListView.as_view()),
    path('todos/create', TodoListViewCreate.as_view()),
    path('todos/<int:pk>', TodoRetrieveUpdateDestroy.as_view()),
    path('todos/<int:pk>/complete', TodoToggleComplete.as_view()),
    path('signup/', signup),
    path('login/', login),


]