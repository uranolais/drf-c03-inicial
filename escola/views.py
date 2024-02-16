from rest_framework import viewsets, generics, filters
from escola.models import Estudante,Curso,Matricula
from escola.serializers import EstudanteSerializer,CursoSerializer,MatriculaSerializer,ListaMatriculasEstudanteSerializer, ListaMatriculasCursoSerializer, EstudanteSerializerV2
from django_filters.rest_framework import DjangoFilterBackend

class EstudantesViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    # filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']
    def get_serializer_class(self):
        print("Valor de request.version:", self.request.version)
        if self.request.version == 'v2': #rota: http://127.0.0.1:8000/estudantes/?version=v2
            return EstudanteSerializerV2
        return EstudanteSerializer

class CursosViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    http_method_names = ['get','post',] #https://docs.djangoproject.com/en/stable/ref/class-based-views/base/#django.views.generic.base.View
  
# localhost:8000/estudante/1/matriculas
    
class ListaMatriculaEstudante(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id = self.kwargs['pk']) #Primary Key
        return queryset
    serializer_class = ListaMatriculasEstudanteSerializer

# localhost:8000/curso/1/matriculas
class ListaMatriculaCurso(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id = self.kwargs['pk']) #Primary Key
        return queryset
    serializer_class = ListaMatriculasCursoSerializer