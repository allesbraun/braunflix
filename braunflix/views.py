from braunflix.models import Program
from braunflix.serializers import ProgramSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    # print(str(queryset.query))
    serializer_class = ProgramSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title']
    filterset_fields = ['kind']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

