from django.urls import path, include

from .views import ExamList, ExamDetail, CreateExam

urlpatterns = [
    path('', ExamList.as_view() ,name="exam_list"),
    path('exam-detail/<int:pk>', ExamDetail.as_view() ,name="exam_detail"),
    path('create-exam/', CreateExam.as_view() ,name="create_exam"),

]
