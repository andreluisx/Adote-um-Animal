# Adote um Animal

<img src="https://github.com/user-attachments/assets/098b5bd7-03c0-4ff3-aff4-a71f55a0e486" alt="Tela Principal" width="450" />

## 🖥️ Funcionalidades

- **Autenticação de usuário**
  
- **Recuperação de senha**
  
- **Editar informações de usuário**
  
- **Listagem completa de animais postados**
  
- **Listas especificas como "Meus animais" e "Animais curtidos"**
  
- **Sistema de paginação, busca e filtro para as listas**


  
## :rocket: Tecnologias Utilizadas

- **Front-end: Django Html, Css, Bootstrap**

- **Back-end: Django**

- **Versionamento: Git e GitHub**
  
- **Banco de dados: Sqlite**

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


