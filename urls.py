from django.urls import path
from .views import submit, ExampleView

urlpatterns = [
    path('', ExampleView.as_view()),
    path('example_submit', submit, name='example_submit'),
    path('example_submit/<name>/', submit, name='example_submit'),
]
