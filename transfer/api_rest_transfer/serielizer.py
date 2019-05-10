from rest_framework.serializers import ModelSerializer
from transfer.models import Transfer
from user.api_rest_user.serielizer import UserSerializer


class TransferSerializer(ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Transfer
        fields = [
            'user', 'pagador_nome', 'pagador_banco', 'pagador_agencia',
            'pagador_conta', 'beneficiario_nome', 'beneficiario_banco',
            'beneficiario_agencia', 'beneficiario_conta', 'valor'
        ]
