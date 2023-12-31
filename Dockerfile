#Pegando uma imagem mais leve do python
FROM python:3.7-slim

#Atualizando e instalando o alien
RUN apt-get update -y && apt-get install alien -y

WORKDIR ./api

# copiando requirements.txt
COPY  requirements.txt .

#Criando os argumento que serão passados no processo de build
ARG DB_USER
ARG DB_PASSWORD
ARG DB_HOST
ARG DB_PORT
ARG DB_SERVICE

# Definindo as variáveis de ambiente com os argumentos
ENV DB_USER='cm'
ENV DB_PASSWORD='cm'
ENV DB_HOST='dbclone.bpark.com.br'
ENV DB_PORT=1521
ENV DB_SERVICE='desenv'

#baixando os drives da oracle
#ADD https://download.oracle.com/otn_software/linux/instantclient/195000/oracle-instantclient19.5-basiclite-19.5.0.0.0-1.x86_64.rpm ./instantclient19.5-basiclite.rpm

#convertendo os arquivos para .deb e removendo após a instalação
#RUN alien -i  --scripts  ./instantclient19.5-basiclite.rpm && rm ./instantclient19.5-basiclite.*

#Instalando os requerimentos da aplicação python e uma lib para conectar ao oracle e removendo o alien, pois não será mais utilizado
#RUN pip install -r requirements.txt && apt-get install libaio1 libaio-dev -y && apt-get remove alien -y

#configurando as variáveis de ambiente dos drives da oracle
#ENV LD_LIBRARY_PATH="/usr/lib/oracle/19.5/client(64)/lib/${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
#ENV ORACLE_HOME="/usr/lib/oracle/19.5/client(64)"
#ENV PATH="/usr/lib/oracle/19.5/;"+${PATH}+""

# Copia o código da aplicação
COPY . .


#RUN chmod +x /api/serve.sh
EXPOSE 8000

#Executa a aplicação
# ENTRYPOINT - allows you to configure a container that will run as an executable.
#ENTRYPOINT ["./api/serve.sh"]
#ENTRYPOINT ["/api/serve.sh"]
CMD ["sh","/api/serve.sh"]
