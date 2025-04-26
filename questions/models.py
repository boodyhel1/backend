from django.db import models

class Question(models.Model):
    QUESTION_TYPES = [
        ('intro', 'مقدمة في علم التجويد'),
        ('letters', 'مخارج الحروف'),
    ]
    
    question_type = models.CharField(max_length=10, choices=QUESTION_TYPES)
    question_text = models.TextField()
    answer = models.CharField(max_length=200)
    explanation = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_text[:50] + "..."