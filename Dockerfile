# Use uma imagem base oficial do Python
FROM python:3.10-slim

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie os arquivos de requerimentos e instale as dependências
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código do aplicativo
COPY . .

# Defina o PYTHONPATH para incluir o diretório de trabalho
ENV PYTHONPATH=/app

# Exponha a porta na qual o aplicativo Flask será executado
EXPOSE 5000

# Defina a variável de ambiente para indicar ao Flask que estamos em modo de desenvolvimento
ENV FLASK_ENV=development

# Comando para rodar a aplicação
CMD ["flask", "run", "--host=0.0.0.0"]
