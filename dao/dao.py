import mysql.connector

from dao.dbConnect import DBConnect
from gestionale.core.cliente import ClienteRecord
from gestionale.core.prodotto import ProdottoRecord


class DAO:

    def getAllProdotti(self):
        # cnx = mysql.connector.connect(
        #     user = "root",
        #     password = "giuliaroot",
        #     host = "127.0.0.1",
        #     database = "sw_gestionale"
        # )
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor(dictionary=True) #mi serve per scorrere i risultati delle query
        cursor.execute("Select * from prodotti")
        row  = cursor.fetchall() #lista di dict

        res=[]
        for p in row:
            res.append(ProdottoRecord(p["nome"], p["prezzo"])) #NOMI CHE HO DATO NEL DATABASE

        #RICORDA DI CHIUDERE LA CONNESSIONE
        cursor.close()
        cnx.close()
        return res

    def getAllCLienti(self):
        # cnx = mysql.connector.connect(
        #     user = "root",
        #     password = "giuliaroot",
        #     host = "127.0.0.1",
        #     database = "sw_gestionale"
        # )
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("Select * from clienti")
        row = cursor.fetchall()

        res = []
        for p in row:
            res.append(ClienteRecord(p["nome"], p["mail"], p["categoria"]))  # NOMI CHE HO DATO NEL DATABASE

        cursor.close()
        cnx.close()
        return res

    def addProdotto(self, prodotto):
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor()
        query ="""insert into prodotti (nome, prezzo) values (%s, %s)"""
        cursor.execute(query, (prodotto.name, prodotto.prezzo_unitario))

        cnx.commit()
        cursor.close()
        cnx.close()
        return

    def addCliente(self, cliente):
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor()
        query ="""insert into clienti (nome, mail, categoria) values (%s, %s)"""

        cursor.execute(query, (cliente.nome, cliente.mail, cliente.categoria))

        cnx.commit()
        cursor.close()
        cnx.close()
        return

    def hasCliente(self, cliente):
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor(dictionary=True)
        query ="Select * from clienti where mail = %s"
        cursor.execute(query, (cliente.mail,))
        row = cursor.fetchall()

        cursor.close()
        cnx.close()
        return len(row)>0 #se row ha almeno una riga, il cliente c'è e non devo metterlo altrimenti si

    def hasProdotto(self, prod):
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor(dictionary=True)
        query = "Select * from prodotti where nome = %s"
        cursor.execute(query, (prod.name,))
        row = cursor.fetchall()

        cursor.close()
        cnx.close()
        return len(row) > 0  # se row ha almeno una riga, il cliente c'è e non devo metterlo altrimenti si


if __name__ == "__main__":
    mydao = DAO()
    mydao.getAllProdotti()