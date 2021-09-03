from django.contrib import admin

from .models import ExamCategory, Questions, Answers


class AnswerInline(admin.StackedInline):
    model = Answers

@admin.register(Questions)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline,
    ]

admin.site.register(ExamCategory)