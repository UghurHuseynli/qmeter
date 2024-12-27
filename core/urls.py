from django.urls import path
from .views import FeedbackView, FeedbackWithoutModelView

urlpatterns = [
    path('feedback/', FeedbackView.as_view(), name='feedback'),
    path('feedback-withoutmodel/', FeedbackWithoutModelView.as_view(), name='feedback-withoutmodel')
]
