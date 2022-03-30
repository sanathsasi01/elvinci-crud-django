from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('', all_students, name='home'),
    path('add-student/', add_student, name="add_student"),
    path('update-student/<int:id>', update_student, name="update_student"),
    path('delete-student/<int:id>', delete_student, name="delete_student"),
]
