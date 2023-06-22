from django.db import models

# Create your models here.

# uma classe para perguntas. pegando dentro do sub-pacote models, o Model
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pup_date = models.DateTimeField('date_published')

class Choise(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE())

    # question_text = uma variavel que vai receber o texto da pergunta
    # CharField = campo de caracteres
    #  pup_date = data da publicação

# esse modelo é o que vai conseguir definir como os dados vão ser tratados do sistema, vai gerar informações pro banco de dados
