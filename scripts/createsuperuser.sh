#!/bin/sh

# Executa o comando Django para criar um superusuário automaticamente
echo "⚙️ Criando superusuário do Django..."

python manage.py shell << END
from django.contrib.auth import get_user_model
import os

User = get_user_model()

username = os.environ.get("DJANGO_SU_NAME")
email = os.environ.get("DJANGO_SU_EMAIL")
password = os.environ.get("DJANGO_SU_PASSWORD")

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("✅ Superusuário criado com sucesso.")
else:
    print("ℹ️ Superusuário já existe.")
END
