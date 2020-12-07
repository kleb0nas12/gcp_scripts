import psycopg2
import ssl
from account import user_acc, password, port, host
class DbOperations:
    def __init__(self,database):
        self.database = database
        self.con = psycopg2.connect(dbname=self.database,user=user_acc,password=password,port=port,host=host,sslcert='',sslkey='',sslrootcert='')


