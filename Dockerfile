# Use a imagem oficial do Python
FROM python:3.9-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie os arquivos necessários para o contêiner
COPY requirements.txt .
COPY app.py .
COPY uber_delivery_trip.py .
COPY templates templates/

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta 5000 para o Flask
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "app.py"]
