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

class VolunteerSubscription(models.Model):
    opportunity = models.ForeignKey(VolunteerOpportunity, on_delete=models.CASCADE, verbose_name='Vaga')
    name = models.CharField(max_length=100, verbose_name='Nome Completo')
    email = models.EmailField(verbose_name='E-mail')
    phone = models.CharField(max_length=20, verbose_name='Telefone')
    message = models.TextField(blank=True, verbose_name='Mensagem')
    status = models.CharField(max_length=20, choices=[('Pendente', 'Pendente'), ('Aprovado', 'Aprovado'), ('Rejeitado', 'Rejeitado')], default='Pendente', verbose_name='Status')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.opportunity.title}'

class AdoptionRequest(models.Model):
    STATUS_CHOICES = (
        ('Pendente', 'Pendente'),
        ('Aprovado', 'Aprovado'),
        ('Rejeitado', 'Rejeitado'),
    )
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, verbose_name='Animal')
    name = models.CharField(max_length=100, verbose_name='Nome Completo')
    email = models.EmailField(verbose_name='E-mail')
    phone = models.CharField(max_length=20, verbose_name='Telefone')
    reason = models.TextField(verbose_name='Por que deseja adotar este animal?')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pendente', verbose_name='Status da Análise')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - Adoção: {self.animal.name}'
