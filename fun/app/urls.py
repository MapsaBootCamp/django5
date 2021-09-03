from django.urls import path, include

from .views import DoctorList, DoctorDetail, CoronaInfoView

urlpatterns = [
    path("doctor-list/", DoctorList.as_view(), name="doctor_list"),
    path("doctor-detail/<int:pk>", DoctorDetail.as_view(), name="doctor_detail"),
    path("corona-info-form", CoronaInfoView.as_view(), name="corona_info_form"),
]
