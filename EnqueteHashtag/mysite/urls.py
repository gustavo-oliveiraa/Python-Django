from django.urls import path
# path = caminho, a url é um caminho
# tem algumas caracteristicas

from . import views
# traz pra mim que tiver no arquivo views

# "lista" de caminhos de como eu gostaria de ver as minhas urls
# urlpatterns = quer criar padroes de url
urlpatterns = [
    path('',views.index, name='index')
    #(vazio (ñ tem nada escrito nele), associado ao arquivo "view".index (o principio que tiver dentro do index), name='index')
]