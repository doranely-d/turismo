from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize= value.size
    
    if filesize > 1048576:
        raise ValidationError("El peso máximo para los archivos es de 1MB")
    else:
        return value
