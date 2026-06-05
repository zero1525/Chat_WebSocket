# Используем официальный легкий образ Python
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Запрещаем Python писать файлы .pyc на диск и буферизировать stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Копируем зависимости и устанавливаем их
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . /app/

# Открываем порт для Daphne
EXPOSE 8000

# Запускаем проект через ASGI-сервер Daphne
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "config.asgi:application"]