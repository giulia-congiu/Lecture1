#creare connessione e restituirla
import mysql.connector

class DBConnect:
    def getConnection(self):

       try: #perchè potrebbe fallire
           cnx = mysql.connector.connect(  # connesione fisica che mi collega al database
                user="root",
                password="giuliaroot",
                host="127.0.0.1",
                database="sw_gestionale"
            )
           return cnx
       except mysql.connector.Error as err:
           print("Non riesco a collegarmi a DB")
           print(err)
           return None