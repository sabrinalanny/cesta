#import cx_Oracle
import oracledb
import os
import platform

#Configurações de conexão
DIALECT = 'oracle'
#SQL_DRIVER = 'cx_oracle'
SQL_DRIVER = 'oracledb'

#Pegando as credenciais via variável de ambiente

USERNAME = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASSWORD')
HOST = os.getenv('DB_HOST')
PORT = os.getenv('DB_PORT')
SERVICE = os.getenv('DB_SERVICE')

#Criando a string de conexão
#connstr = f"{USERNAME}/{PASSWORD}@{HOST}:{PORT}/{SERVICE}"

#Conectando ao SGBD
#conn = cx_Oracle.connect(connstr,encoding = "UTF-8", nencoding = "UTF-8")

#Criando um cursor
#cursor = conn.cursor()

#Rodando uma Query para teste
#cursor.execute("select sysdate from dual")
#result = cursor.fetchall()
#for row in result:
 #   print(result)


d = None  # default suitable for Linux
if platform.system() == "Darwin" and platform.machine() == "x86_64":   # macOS
  d = os.environ.get("HOME")+("/Downloads/instantclient_12_2")
elif platform.system() == "Windows":
  d = r"C:\oracle\instantclient_12_2"
oracledb.init_oracle_client(lib_dir=d)


un = 'cm' #os.environ.get('PYTHON_USERNAME')
pw = 'cm' #os.environ.get('PYTHON_PASSWORD')
host           = 'dbclone.bpark.com.br'
port           =  1521
service_name   = 'desenv'

params = oracledb.ConnectParams(host=host, port=port, service_name=service_name)
with oracledb.connect(user=un, password=pw, params = params) as connection:
    with connection.cursor() as cursor:
        sql = """select sysdate from dual"""
        for r in cursor.execute(sql):
            print(r)
