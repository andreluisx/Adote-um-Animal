# Adote um Animal

## Estrutura do projeto

Estrutura do repositorio:

* **Front-end**: Templates dentro das pastas de apps.

* **Back-end**: A pasta ourAnimal tem todas as configurações do projeto.

### Rodar o projeto

```
python -m venv venv
venv/Scripts/activate
pip install requirements.txt
python manage.py runserver
```

### Configurações adicionais

```
criar pasta ".env"
ajustar as variáveis de ambiente
```

#### Criar static files

```
python manage.py collectstatic --noinput
```

### Migrations

#### Criar arquivos de migração

```
python manage.py makemigrations
```

#### Migrar base de dados

```
python manage.py migrate
```

### Dependencies

#### Criar superuser

```
python manage.py createsuperuser
```

### Base de dados

Base de dados usada:

```
Sqlite
```

## :rocket: Tecnologias Utilizadas

- **Front-end: Django Html, Css, Bootstrap**

- **Back-end: Django**

- **Versionamento: Git e GitHub**
  
- **Banco de dados: Sqlite**
