
from django.test import TestCase
from .models import User


class UsuarioTestModel(TestCase):

    def setUp(self):
        self.user = User.objects.create(nome='Gilson Leite', cnpj='05247316000104')

    def test_models_usuario(self):
        self.assertEqual(self.user.nome, 'Gilson Leite')
        self.assertEqual(self.user.cnpj, '05247316000104')

    def test_models_max_length(self):
        self.assertEqual(self.user._meta.get_field('cnpj').max_length, 14)
        self.assertEqual(self.user._meta.get_field('nome').max_length, 128)

    def test_models_verbose_name(self):
        self.assertEqual(self.user._meta.get_field('cnpj').verbose_name, 'cnpj')
        self.assertEqual(self.user._meta.get_field('nome').verbose_name, 'nome')
