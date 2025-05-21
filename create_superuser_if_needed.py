from django.contrib.auth import get_user_model

User = get_user_model()

# Criação do superusuário automaticamente (caso não exista)
if not User.objects.filter(username="blog_univesp").exists():
    User.objects.create_superuser("blog_univesp", "givaldowanda@gmail.com", "6IuFj1XCLXY497IwUY598HigynrwGzBp")
