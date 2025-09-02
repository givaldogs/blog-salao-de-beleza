from django.shortcuts import render, redirect
from .models import Feedback

def enviar_feedback(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        if tipo in dict(Feedback.FEEDBACK_CHOICES).keys():
            Feedback.objects.create(tipo=tipo)
        # Corrigido para incluir o namespace do app
        return redirect('avaliacoes:feedback_enviado')

    return render(request, 'avaliacoes/feedback.html')


def feedback_enviado(request):
    return render(request, 'avaliacoes/feedback_enviado.html')
