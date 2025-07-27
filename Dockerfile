
FROM python:3.10

# Definir o diretório de trabalho no container
ENV APP_HOME /app
WORKDIR $APP_HOME

# Instalar as dependências da aplicação
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar os arquivos da aplicação para o container
COPY . ./

EXPOSE 8080

# Comando para rodar a aplicação
CMD python main.py
