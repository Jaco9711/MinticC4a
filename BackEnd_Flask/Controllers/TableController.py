from Repositories.TableRepository import TableRepository
from Models.Table import Table

class TableController():
    
    def __init__(self):
        self.RepositoryTable = TableRepository()
    
    def index(self):
        return self.RepositoryTable.findAll()
    
    def create(self, infoTable):
        newTable = Table(infoTable)
        return self.RepositoryTable.save(newTable)
    
    def show(self, id):
        theTable = Table(self.RepositoryTable.findById(id))
        return theTable.__dict__
    
    def update(self, id, infoTable):
        TableCurrent = Table(self.RepositoryTable.findById(id))
        TableCurrent.numero = infoTable["numero"]
        TableCurrent.cantidad_inscritos = infoTable["cantidad_inscritos"]
        return self.RepositoryTable.save(TableCurrent)
    
    def delete(self, id):
        return self.RepositoryTable.delete(id)
