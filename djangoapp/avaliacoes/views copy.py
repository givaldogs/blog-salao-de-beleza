from django.shortcuts import render, redirect
from .models import Feedback
from collections import Counter

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


def feedback_dashboard(request):
    feedbacks = Feedback.objects.all().order_by('-data_hora')

    total = feedbacks.count()
    contagem = Counter(feedbacks.values_list('tipo', flat=True))

    context = {
        'total': total,
        'bom': contagem.get('good', 0),
        'neutro': contagem.get('neutral', 0),
        'ruim': contagem.get('bad', 0),
        'feedbacks': feedbacks[:10],  # últimos 10 feedbacks
    }

    return render(request, 'avaliacoes/dashboard.html', context)
