# 💇‍♀️ Agendamento de Salão

Aplicação web desenvolvida em **Django** para permitir que uma recepcionista agende serviços para clientes com um profissional específico, em uma data e horário definidos, além de atualizar o status desses serviços.

---

## 📌 Funcionalidades

- **Cadastro de usuários**
- **Cadastro de funcionários**
- **Cadastro de serviços oferecidos pelo salão**
- **Agendamento de serviços com profissional e horário definidos**
- **Consulta e atualização de agendamentos**
- **Painel administrativo padrão do Django para gestão dos dados**

---

## 🚀 Tecnologias utilizadas

- [Python](https://www.python.org/) `3.12.10`
- [Django](https://www.djangoproject.com/) `5.2.5`
- Banco de dados padrão: **SQLite** (padrão do Django)


---

## ⚙️ Como rodar o projeto localmente

1. **Clone o repositório**
git clone https://github.com/PedroFoll/agendamento_Django.git
cd agendamento_Django

2. **Crie e ative o ambiente Virtual**

        python -m venv venv

**Linux/Mac**
    
        source venv/bin/activate
**Windows**

        venv\Scripts\activate

3. **Instale as dependencias**

        pip install django==5.2.5

4. **Realize as migrações**

        python manage.py makemigrations
        python manage.py migrate

5. **Execute o Servidor**

        python manage.py runserver

### Após todos esses passos, será possível acessar às URLS disponibilizadas

1. **A url padrão do projeto é:**

    http://127.0.0.1:8000/

    Ao acessar, você se encontrará com a home da aplicação, com uma barra de navegação, entre os serviçõs disponiveis para utilização.
