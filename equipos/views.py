from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from equipos.serializers import EquiposSerializer
from fmeca.serializers import FmecaSerializer
from equipos.models import Equipo
from fmeca.models import FMeca
from equipos.permission import IsAdminOrReadOnly
from rest_framework import permissions
# Create your views here.
from django.http import JsonResponse

class EquipoViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    serializer_class = EquiposSerializer
    queryset = Equipo.objects.all()


class EquiposFallasDetails(APIView):
    def get(self, request, id=0):
        if id > 0:
            #queryset_fmeca = FMeca.objects.filter(equipo=id).all()
            queryset_machine = Equipo.objects.filter(id=id).all()
        else:
            queryset_fmeca = FMeca.objects.all()

        serializer_machine = EquiposSerializer(queryset_machine, many=True)

        return Response(serializer_machine.data)



