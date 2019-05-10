from django.test import TestCase
from .models import Transfer
from .models import User
from django.utils import timezone


class TransferenciaTestModel(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            nome='Gilson Leite', cnpj='05247316000104')

        self.transfer = Transfer.objects.create(
            user_id=self.user.id, pagador_nome='Gilson Leite',
            pagador_banco='Banco Bradesco', pagador_agencia='237',
            pagador_conta='3131', beneficiario_nome='Paulo Roberto',
            beneficiario_banco='Banco Bradesco', beneficiario_agencia='237',
            beneficiario_conta='3245', valor=0,
            tipo='1', status='1', data=timezone.now()

        )

    def test_models_valid_usuario(self):
        self.assertEqual(self.user.id, self.transfer.user.id)

    def test_models_max_length(self):
        self.assertEqual(self.transfer._meta.get_field('valor').max_digits, 8)
        self.assertEqual(self.transfer._meta.get_field('valor').decimal_places, 2)
        self.assertEqual(self.transfer._meta.get_field('data').auto_now_add, True)







