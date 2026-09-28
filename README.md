# Ajuda Animais (Django)

Este é um projeto desenvolvido em **Python + Django** criado para facilitar a divulgação de adoção de animais e oportunidades de voluntariado em uma associação de proteção animal. 

O front-end foi construído utilizando **Bootstrap 5** para garantir um visual moderno e responsivo.

## Pré-requisitos

Certifique-se de ter o [Python](https://www.python.org/downloads/) (versão 3.8 ou superior) instalado na sua máquina.

## Passo a Passo para Instalação

1. **Clone ou acesse o repositório/pasta do projeto**
2. **Crie e ative um ambiente virtual**
   - No Windows:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - No Linux/Mac:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```
4. **Aplique as migrações no banco de dados**
   ```bash
   python manage.py migrate
   ```
5. **Crie um superusuário (opcional, para acessar a área administrativa)**
   ```bash
   python manage.py createsuperuser
   ```
6. **Inicie o servidor de desenvolvimento**
   ```bash
   python manage.py runserver
   ```
7. Acesse o sistema no seu navegador no endereço: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Funcionalidades
- **Área Pública**: Visualização das listagens de Animais disponíveis para Adoção e Vagas de Voluntariado divididas em abas (*Tabs*).
- **Painel Administrativo**: Área segura (acessível em `/admin/`) para gerenciar as inserções e remoções de animais e oportunidades de voluntariado.

## Tecnologias Utilizadas
- **Backend:** Python e Django
- **Frontend:** HTML5, CSS3, Bootstrap 5, Bootstrap Icons
- **Banco de Dados:** SQLite (padrão do Django para desenvolvimento)
