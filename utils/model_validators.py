from django.core.exceptions import ValidationError

def validade_png(image):
    if not image.name.lower().endswith('.png'):
        raise ValidationError('Imagem precisa ser png')
