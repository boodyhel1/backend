from rest_framework import generics
from rest_framework.response import Response
from .models import Question
from .serializers import QuestionSerializer
import random
from rest_framework.views import APIView

class RandomQuestionView(APIView):
    def get(self, request):
        questions = list(Question.objects.all())
        if not questions:
            return Response({"error": "No questions available"}, status=404)
        question = random.choice(questions)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

class CheckAnswerView(generics.GenericAPIView):
    serializer_class =  QuestionSerializer
    
    def get(self, request, question_id):
        try:
            question =  Question.objects.get(pk=question_id)
            serializer = self.get_serializer(question)
            return Response(serializer.data)
        except  Question.DoesNotExist:
            return Response({"error": "Question not found"}, status=404)