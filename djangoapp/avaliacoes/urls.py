from django.urls import path
from . import views  # importa as views do app avaliacoes

app_name = 'avaliacoes'  # ← ESSENCIAL para usar {% url 'avaliacoes:feedback_enviado' %}

urlpatterns = [
    path('', views.enviar_feedback, name='enviar_feedback'),
    path('enviado/', views.feedback_enviado, name='feedback_enviado'),
]
