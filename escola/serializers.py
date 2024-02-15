from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula
from escola.validators import cpf_invalido, nome_invalido, celular_valido

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id','nome','email','cpf','data_nascimento','celular']
    
    def validate(self, data): #esse data não é obrigatório ter esse nome
        if cpf_invalido(data['cpf']):
            raise serializers.ValidationError({'cpf':'Número de CPF inválido'})
        if nome_invalido(data['nome']):
            raise serializers.ValidationError({'nome':'O nome só pode ter letras'})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':'O número de celular deve seguir este modelo: 86 99999-9999 (respeitando os espaços e traço)'})
        return data

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'
    

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []

# localhost:8000/estudante/1/matriculas
class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()#To vendo se ainda vou usar isso daqui
    class Meta:
        model = Matricula
        fields = ['curso','periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()
    # get_<nome_do_campo>_display() https://docs.djangoproject.com/pt-br/4.2/ref/models/instances/#extra-instance-methods

# localhost:8000/curso/1/matriculas
class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source = 'estudante.nome')
    class Meta:
        model = Matricula
        fields = ['estudante_nome',]

class EstudanteSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id','nome','email','celular']
