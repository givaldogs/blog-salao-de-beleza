from pathlib import Path
 
from django.conf import settings
from PIL import Image 
 
def resize_image(image_django, new_width=800, optimize=True, quality=60):
    #image_path = Path(settings.MEDIA_ROOT / image_django.name).resolve()
    # Garante que MEDIA_ROOT seja tratado como Path
     media_root = Path(settings.MEDIA_ROOT)
     image_path = (media_root / image_django.name).resolve()  # Agora usamos Path corretamente    

    # Verifique se o arquivo realmente existe
     if not image_path.exists():
        raise FileNotFoundError(f"A imagem {image_path} não foi encontrada.")

     image_pillow = Image.open(image_path)
     original_width, original_height = image_pillow.size

    # Se a largura original for menor ou igual ao novo tamanho, não redimensione
     if original_width <= new_width:
         image_pillow.close()
         return image_pillow
 
    # Calcule a nova altura para manter a proporção
     new_height = round(new_width * original_height / original_width)
 
     # Atualizado para a versão mais recente do Pillow
     # Redimensione a imagem
     new_image = image_pillow.resize((new_width, new_height), Image.Resampling.LANCZOS)
 
     new_image.save(
         image_path,
         optimize=optimize,
         quality=quality,
     )
     # Feche as imagens para liberar os recursos

     image_pillow.close()
     new_image.close()
 
     return new_image