from django.urls import path
from .views import first_task_view, second_task_view, get_iban_history, third_task_view, fourth_task_view

urlpatterns = [
    path('validate/', first_task_view, name='first_task_view'),
    path('real-time-validation/', second_task_view, name='second_task_view'),
    path('history/', get_iban_history, name='get_iban_history'),
    path('test-driven-development-validate/', third_task_view, name='third_task_view'),
    path('suggest-correct-iban/', fourth_task_view, name='fourth_task_view')
]