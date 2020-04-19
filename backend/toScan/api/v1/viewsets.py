from rest_framework import authentication
from toScan.models import ListToValidate
from .serializers import ListToValidateSerializer
from rest_framework import viewsets


class ListToValidateViewSet(viewsets.ModelViewSet):
    serializer_class = ListToValidateSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = ListToValidate.objects.all()
