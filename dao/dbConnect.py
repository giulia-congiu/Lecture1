#creare connessione e restituirla
import pathlib

import mysql.connector
from click import option


class DBConnect:
    _mypool = None

    def __init__(self):
        raise RuntimeError("Attenzione non devi creare un istanza di questa classe usa i metodi di classe")

    @classmethod
    def getConnection(cls):
       if cls._myPool is None:
           try: #perchè potrebbe fallire
               # cnx = mysql.connector.connect(  # connesione fisica che mi collega al database
               #      user="root",
               #      password="giuliaroot",
               #      host="127.0.0.1",
               #      database="sw_gestionale"
               #  )
               cls._myPool = mysql.connector.pooling.MySQLConnectionPool(
                   user = "root",
                   password="giuliaroot",
                   host="127.0.0.1",
                   database="sw_gestionale",
                   pool_size= 3,
                   pool_name ="myPool",
                   option_files = f"{pathlib.Path(__file__).resolve().parent}/connector.cfg"
               )
               return cls._myPool.get_connection()

           except mysql.connector.Error as err:
               print("Non riesco a collegarmi a DB")
               print(err)
               return None
       else:
           return cls._mypool.get_connection()
           #allora rido la connessione
