from django.contrib.staticfiles.finders import AppDirectoriesFinder


class CustomAppDirectoriesFinder(AppDirectoriesFinder):
    source_dir = 'resume_static'
