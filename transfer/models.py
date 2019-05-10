from django.db import models
from user.models import User


TIPO = (
    ('1', 'CC'),
    ('2', 'TED'),
    ('3', 'DOC'),
)

STATUS = (
    ('1', 'OK'),
    ('2', 'ERRO'),
)


class Transfer(models.Model):
    user = models.ForeignKey(User, related_name='user',
                             on_delete=models.CASCADE)
    pagador_nome = models.CharField(max_length=128)
    pagador_banco = models.CharField(max_length=3)
    pagador_agencia = models.CharField(max_length=4)
    pagador_conta = models.CharField(max_length=6)
    beneficiario_nome = models.CharField(max_length=128)
    beneficiario_banco = models.CharField(max_length=3)
    beneficiario_agencia = models.CharField(max_length=4)
    beneficiario_conta = models.CharField(max_length=6)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    tipo = models.CharField(max_length=1, choices=TIPO)
    status = models.CharField(max_length=1, choices=STATUS)
    dasabilitado = models.BooleanField(
        default=False, help_text='Deixar ativo para exclusao logica')
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pagador_nome


    

