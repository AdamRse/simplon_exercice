FROM python:3.12-slim

WORKDIR /app

# Copie des dépendances en premier (cache Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code source
COPY src/ ./src/

CMD ["python", "src/main.py"]
