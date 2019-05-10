from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serielizer import *
from transfer.models import *


class TransferViewSet(ModelViewSet):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Transfer.objects.filter(dasabilitado=False)

    def destroy(self, request, *args, **kwargs):
        _obj = self.get_object()
        _obj.dasabilitado = True
        _obj.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
