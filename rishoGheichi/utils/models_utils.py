def model_image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    file_type = filename.split('.')[-1]
    username = instance.user.email.split("@")[0]
    return f'{instance.__class__.__name__}/{instance.id}_{username}.{file_type}'

