def model_image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return f'{instance.__class__.__name__}/{instance.id}_{instance}'

