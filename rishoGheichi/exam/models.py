from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ExamCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Questions(models.Model):
    LEVEL_CHOICE = (
        ('e', 'easy'),
        ('m', 'middle'),
        ('a', 'advanced'),
    )
    level = models.CharField(max_length=1, choices=LEVEL_CHOICE)
    title = models.CharField(max_length=500)
    category = models.ForeignKey(ExamCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"


class Answers(models.Model):
    question = models.ForeignKey(Questions, related_name="answer", on_delete = models.CASCADE)
    is_correct = models.BooleanField(default=False)
    matn_gozineh = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.id}-{self.question.title}"

    def save(self, *args, **kwargs):
        question_answers = self.question.answer.all()
        if len(question_answers) > 3:
            raise Exception("bish az chartai")
        if len(question_answers) == 3:
            if not question_answers.filter(is_correct=True).exists() and not self.is_correct:
                raise Exception("hadeaghal ye javab dorost mikhad")
        if question_answers.filter(is_correct=True).exists() and self.is_correct:
            raise Exception("soal nemitavanad bish az do javab sahih dashte bashe")

        return super().save(*args, **kwargs)


class Exam(models.Model):
    category = models.ForeignKey(ExamCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField(null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category.name}-{self.user.username}-{self.create_time}"


class ExamItems(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.RESTRICT)
    user_answer = models.ForeignKey(Answers, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}-{self.exam.id}"
