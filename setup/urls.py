from django.contrib import admin
from django.urls import path,include
from escola.views import EstudantesViewSet,CursosViewSet,MatriculaViewSet,ListaMatriculaEstudante,ListaMatriculaCurso
from rest_framework import routers

router = routers.DefaultRouter()
router.register('estudantes',EstudantesViewSet,basename='Estudantes')
router.register('cursos',CursosViewSet,basename='Cursos')
router.register('matriculas',MatriculaViewSet,basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('estudante/<int:pk>/matriculas',ListaMatriculaEstudante.as_view()),
    path('curso/<int:pk>/matriculas',ListaMatriculaCurso.as_view()),
]
