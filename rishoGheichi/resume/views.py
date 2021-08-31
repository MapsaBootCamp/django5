from django.shortcuts import render

def show_resume(request):
    return render(request, 'resume/index.html', {})