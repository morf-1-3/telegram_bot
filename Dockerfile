# Використовуємо офіційний Python-образ
FROM python:3.12.3

# Встановлюємо робочу директорію
WORKDIR /app

ENV PYTHONPATH=/app
# Копіюємо файли проєкту
COPY . .

# Встановлюємо залежності для обох сервісів
RUN pip install --no-cache-dir -r requirements.txt


# Вказуємо змінні середовища
ENV PYTHONUNBUFFERED=1

# Запуск контейнера
CMD ["sh", "-c", "cd api && uvicorn main:app --host 0.0.0.0 --port 8000 && python bot/bot.py"]
