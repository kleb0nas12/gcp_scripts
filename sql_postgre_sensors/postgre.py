import psycopg2
import ssl
from account import user_acc, password, port, host, database
class DbOperations:
    def __init__(self):
        self.database = database
        try:
            self.con = psycopg2.connect(dbname=database,user=user_acc,password=password,port=port,host=host,sslcert='/home/ubuntu/workingdir/gcp_scripts/sql_postgre_sensors/ssl/ssl-cert.crt',sslkey='/home/ubuntu/workingdir/gcp_scripts/sql_postgre_sensors/ssl/ssl-key.key',sslrootcert='/home/ubuntu/workingdir/gcp_scripts/sql_postgre_sensors/ssl/ca-cert.crt')
        except Exception as e:
            print(e)
        self.cur = self.con.cursor()



    ## method to commit data to specific project 'telemetry data'

    def omit_data(self,time,cpu,cam,out,hum):
        try:
            self.cur.execute("INSERT INTO day_2020_12_07 (time,cpu_temp,cam_temp,out_temp,out_hum) VALUES (%s,%s, %s, %s, %s)",(time,cpu,cam,out,hum))
            self.con.commit()
            print('Data transfer has been executed successfully')
        except Exception as e:
            print('Error accured :',e)
        finally:
            pass
        



