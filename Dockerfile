FROM nginx:latest
COPY app/templates/index.html /usr/share/nginx/html/

# Atualize o sistema e instale o PostgreSQL e o Python
RUN apt-get update && \
    apt-get install -y postgresql python3 python3-pip && \
    apt-get clean

# Exponha a porta do PostgreSQL
EXPOSE 5432

# Crie o diretório do PostgreSQL e configure-o para permitir conexões remotas
RUN mkdir -p /etc/postgresql/12/main/ && \
    echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/12/main/pg_hba.conf && \
    echo "listen_addresses='*'" >> /etc/postgresql/12/main/postgresql.conf

# Inicie o PostgreSQL quando o contêiner for iniciado
CMD service postgresql start && \
    /bin/bash
