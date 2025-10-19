from django.shortcuts import render, redirect
from .models import Feedback
from collections import Counter
from django.utils import timezone
from datetime import timedelta

def enviar_feedback(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        if tipo in dict(Feedback.FEEDBACK_CHOICES).keys():
            Feedback.objects.create(tipo=tipo)
        return redirect('avaliacoes:feedback_enviado')
    
    return render(request, 'avaliacoes/feedback.html')


def feedback_enviado(request):
    return render(request, 'avaliacoes/feedback_enviado.html')


def feedback_dashboard(request):
    feedbacks = Feedback.objects.all().order_by('-data_hora')

    # Totais para gráfico de pizza
    total = feedbacks.count()
    contagem = Counter(feedbacks.values_list('tipo', flat=True))

    # Últimos 7 dias
    hoje = timezone.localtime().date()
    dias = [hoje - timedelta(days=i) for i in range(6, -1, -1)]  # Ex: [11/10, ..., 17/10]
    dias_formatados = [dia.strftime('%d/%m') for dia in dias]

    # Inicializa os dados por dia
    dados_por_dia = {dia: {'good': 0, 'neutral': 0, 'bad': 0} for dia in dias}

    for feedback in feedbacks:
        data_feedback = timezone.localtime(feedback.data_hora).date()
        if data_feedback in dados_por_dia:
            dados_por_dia[data_feedback][feedback.tipo] += 1

    # Prepara listas para o gráfico de barras
    bom_por_dia = [dados_por_dia[d]['good'] for d in dias]
    neutro_por_dia = [dados_por_dia[d]['neutral'] for d in dias]
    ruim_por_dia = [dados_por_dia[d]['bad'] for d in dias]

    context = {
        'total': total,
        'bom': contagem.get('good', 0),
        'neutro': contagem.get('neutral', 0),
        'ruim': contagem.get('bad', 0),
        'feedbacks': feedbacks[:10],
        'dias': dias_formatados,
        'bom_por_dia': bom_por_dia,
        'neutro_por_dia': neutro_por_dia,
        'ruim_por_dia': ruim_por_dia,
    }

    return render(request, 'avaliacoes/dashboard.html', context)
