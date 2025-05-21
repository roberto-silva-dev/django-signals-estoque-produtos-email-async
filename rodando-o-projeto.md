## 🚀 Rodando o Projeto

1️⃣ Clone o repositório:  
```bash
git clone https://github.com/roberto-silva-dev/django-signals-estoque-produtos-email-async.git
cd core
```

2️⃣ Instale as dependências:  
```bash
pip install -r requirements.txt
```
### Configre o arquivo .env com as credenciais do servidor de e-mail

3️⃣ Realize as migrações:  
```bash
python manage.py makemigrations
python manage.py migrate
```

4️⃣ Rode o servidor:  
```bash
python manage.py runserver
```

Acesse o sistema: [http://127.0.0.1:8000](http://127.0.0.1:8000)


- Rode o consumidor de tarefas (worker)
```bash
celery -A core worker --loglevel=info --concurrency=1 --pool=solo
```

- Rode o flower para acompanhar a execução das tarefas
```bash
celery -A core flower --port=5555
```
Acesse em `http://localhost:5555`

