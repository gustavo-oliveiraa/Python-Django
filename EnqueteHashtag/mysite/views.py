from django.shortcuts import render
from django.http import HttpResponse
# O HttpResponse é uma classe do Django que representa uma resposta HTTP que pode ser enviada de volta ao cliente

# Create your views here.

def index(request):
    return HttpResponse("Olá esse é o meu primeiro site")


# A pagina inicial do sistema leva o nome de "index"
# request = requisição
# return = retornar
# HttpResponse = resposta no site

# precisa atrelar essa vizualização a uma "url"
