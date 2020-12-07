import psycopg2
import ssl
from account import user_acc, password, port, host, database
class DbOperations:
    def __init__(self):
        self.database = database
        self.con = psycopg2.connect(dbname=database,user=user_acc,password=password,port=port,host=host,sslcert='~/ssl/ssl-cert.crt',sslkey='~/ssl/ssl-key.key',sslrootcert='~/ssl/ca-cert.crt')
        self.cur = self.con.cursor()



    ## method to commit data to specific project 'telemetry data'

    def omit_data(self,time,cpu,cam,out,hum):
        try:
            self.cur.execute("INSERT INTO telemetry_data VALUES (%s,%s, %s, %s, %s)",(time,cpu,cam,out,hum))
            print('Data transfer has been executed successfully')
        except Exception as e:
            print('Error accured :',e)
        finally:
            pass
        



