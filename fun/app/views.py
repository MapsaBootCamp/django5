from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, DetailView
from django.views import View
from django.urls import reverse
from django.views.generic.edit import FormView

from .models import Doctor, CoronaInforamtion
from .forms import CoronaInfoForm


class DoctorList(ListView):
    model = Doctor
    template_name = "doctor_list.html"
    context_object_name = "doctor_list"
    paginate_by = 2

    def get_queryset(self):
        return super().get_queryset().filter(name__contains="sh")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ashkan"
        return context


class DoctorDetail(DetailView):
    model = Doctor
    template_name = "doctor_detail.html"
    context_object_name = "doctor_detail"


# class CoronaInfoView(View):
#     def get(self, request):
#         form = CoronaInfoForm()
#         return render(request, "corona_info_form.html", {"form": form})

#     def post(self, request):
#         form = CoronaInfoForm(request.POST)

#         if form.is_valid():
#             print(form.cleaned_data["city"])
#             form.save()
#             return redirect(reverse('doctor_list'))

#         return render(request, "corona_info_form.html", {"form": form})


class CoronaInfoView(FormView):
    template_name = "corona_info_form.html"
    form_class = CoronaInfoForm
    success_url = "doctor-list"
