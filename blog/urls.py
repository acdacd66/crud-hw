from django.contrib import admin
from django.urls import path
import blogapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',    blogapp.views.home, name='home'),
    path('post/<int:post_id>', blogapp.views.detail, name="detail"),
    path('new/', blogapp.views.new, name='new'),
    path('create/', blogapp.views.create, name='create'),
    path('edit/<int:post_id>', blogapp.views.edit, name="edit"),
    path('update/<int:post_id>', blogapp.views.update, name="update"),
    path('delete/<int:post_id>', blogapp.views.delete, name="delete"),
]
