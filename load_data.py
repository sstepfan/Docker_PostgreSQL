import psycopg2
import pandas as pd
from sqlalchemy import create_engine

def load(file, table_name):
    # read csv
    data = pd.read_csv(file, encoding='unicode_escape')

    user = 'postgres'
    passwd = 'postgres'
    hostname = 'localhost'
    database = 'peserta_training'

    conn_string = f'postgresql://{user}:{passwd}@{hostname}:5432/{database}'

    db = create_engine(conn_string)
    conn = db.connect()

    data.to_sql(table_name, con=conn, if_exists='replace',index=False)

if __name__ == '__main__':
    load('/Users/mac/Desktop/Digital Skola/HW Project_3/ID_NamaPeserta.csv', 'latihan_nama_peserta')