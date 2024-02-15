import re #próprio do python
from validate_docbr import CPF

def cpf_invalido(numero_cpf): #já começar com número de cpf
    cpf = CPF()
    cpf_valido = cpf.validate(numero_cpf)
    return not cpf_valido

def nome_invalido(nome):
    return not nome.isalpha()

# 86 99999-9999
def celular_valido(numero): #melhor numero que celular, mudar para VALIDO e colocar o not no serializer
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, numero) #retorna uma lista contendo todas as correspondências encontradas na string
    # se não bater o modelo com o número, resposta = [] e [] = False
    # resposta = ['86 99999-9999'] = True ou re = [] e [] = False
    print(resposta) # mostrar a resposta no print
    return resposta