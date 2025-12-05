FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Instala dependências do sistema
RUN apt-get update && apt-get install -y libpq-dev gcc

# Instala Python libs
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

# Usa Gunicorn para produção (Mais robusto que o runserver)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application"]