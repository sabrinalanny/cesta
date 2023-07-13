import oracledb
import os
import platform


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


