from django.db import models

# Create your models here.
class Feedback(models.Model):
    FEEDBACK_CHOICES = [
        ('good', 'Bom'),
        ('neutral', 'Neutro'),
        ('bad', 'Ruim'),
    ]

    tipo = models.CharField(max_length=10, choices=FEEDBACK_CHOICES)
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.data_hora.strftime('%d/%m/%Y %H:%M')}"  # type: ignore

