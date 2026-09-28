from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    species = models.CharField(max_length=50, verbose_name="Espécie")
    age = models.CharField(max_length=50, verbose_name="Idade")
    description = models.TextField(verbose_name="Descrição")
    image_url = models.URLField(blank=True, null=True, verbose_name="URL da Imagem")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.species}"

class VolunteerOpportunity(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título da Vaga")
    schedule = models.CharField(max_length=100, verbose_name="Horário")
    description = models.TextField(verbose_name="Descrição")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
