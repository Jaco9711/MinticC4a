from Repositories.ResultRepository import ResultRepository
from Repositories.TableRepository import TableRepository
from Repositories.AspirantRepository import AspirantRepository

from Models.Result import Result
from Models.Aspirant import Aspirant
from Models.Table import Table

class ResultController():
    def __init__(self):
        self.RepositoryResult = ResultRepository()
        self.RepositoryAspirant = AspirantRepository()
        self.RepositoryTable = TableRepository()

    def index(self): 
        return self.RepositoryResult.findAll()

    def create(self, infoResult, id_Table, id_Aspirant):
        newtheAspirantResult = Result(infoResult)
        theTable = Table(self.RepositoryTable.findById(id_Table))
        theAspirant = Aspirant(self.RepositoryAspirant.findById(id_Aspirant))
        newtheAspirantResult.Table = theTable
        newtheAspirantResult.Aspirant = theAspirant
        return self.RepositoryResult.save(newtheAspirantResult)

    def show(self, id):
        elResult = Result(self.RepositoryResult.findById(id))
        return elResult.__dict__

    def update(self, id, infoResult, id_Table, id_Aspirant):
        elResult = Result(self.RepositoryResult.findById(id))
        theTable = Table(self.RepositoryTable.findById(id_Table))
        theAspirant = Aspirant(self.RepositoryAspirant.findById(id_Aspirant))
        elResult.Table = theTable
        elResult.Aspirant = theAspirant
        return self.RepositoryResult.save(elResult)

    def delete(self, id):
        return self.RepositoryResult.delete(id)

    def getListarAspirantsTable(self, id_Table):
        return self.RepositoryResult.getListAspirantsinscribedTable(id_Table)

    def getListarTablesDesignedAspirant(self, id_Aspirant):
        return self.RepositoryResult.getListTablesAspirantsigned(id_Aspirant)

    def getMayorCedula(self):
        return self.RepositoryResult.getNumeroCedulaMayorAspirant()