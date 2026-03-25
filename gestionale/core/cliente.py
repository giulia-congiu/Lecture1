from dataclasses import dataclass

#corredo minimo che deve avere un DTO
@dataclass
class ClienteRecord:
    nome: str
    mail: str
    categoria: str

    def __hash__(self):
        #per convenzione due istanze sono lo stesso oggetto se la chiave PRIMARIA nel database è la stessa
        return hash(self.mail)

    def __eq__(self, other):
        #è ragionevole dire che due oggetti sono uguali se in questo caso hanno stessa email
        self.mail == other.mail

    def __str__(self):
        return f"{self.nome} -- {self.mail} ({self.categoria})"