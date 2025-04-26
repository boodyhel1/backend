from django.urls import path
from .views import RandomQuestionView, CheckAnswerView

urlpatterns = [
    path('random/', RandomQuestionView.as_view(), name='random-question'),
    path('<int:question_id>/check/', CheckAnswerView.as_view(), name='check-answer'),
]