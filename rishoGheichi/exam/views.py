from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from .models import ExamCategory, Exam


class ExamList(View):
    def get(self, request):
        qs = ExamCategory.objects.all()

        context = {
            "exams_list": qs
        }
        return render(request, 'exam/exam_lists.html', context)


class ExamDetail(LoginRequiredMixin, View):
    def get(self, request, pk):
        exam_cat_obj = get_object_or_404(ExamCategory, id=pk)
        exam_qs = Exam.objects.filter(category=exam_cat_obj, user=request.user).order_by("create_time")
        context = {
            "exam_category": exam_cat_obj.name,
            "exams_list": exam_qs,

        }
        return render(request, 'exam/exam_detail.html', context)


class CreateExam(LoginRequiredMixin, View):
    # TODO
    def get(self, request):
        pass
