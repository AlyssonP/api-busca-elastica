FROM python:3.11-slim-buster

RUN apt-get update && \
    apt-get install -y poppler-utils libpq-dev gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Define o argumento de build para o ambiente
ARG ENVIRONMENT=production

COPY requirements.txt ./
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

EXPOSE 5050

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
