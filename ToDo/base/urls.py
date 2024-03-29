from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskDelete, TaskEdit, CustomLoginViews,RegisterPage

from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/', CustomLoginViews.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='tasks'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-edit/<int:pk>/', TaskEdit.as_view(), name='task-edit'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete')
]
