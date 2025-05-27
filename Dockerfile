# Imagem base
FROM python:3.12-slim

# Diretório de trabalho
WORKDIR /app

# Copia os arquivos
COPY . /app

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Exposição da porta
EXPOSE 5001

# Comando de execução
CMD ["python", "app/app.py"]
