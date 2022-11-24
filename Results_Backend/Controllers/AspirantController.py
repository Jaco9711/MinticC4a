from Repositories.AspirantRepository import AspirantRepository
from Repositories.PartyRepository import PartyRepository
from Models.Aspirant import Aspirant
from Models.Party import Party

class AspirantController():
    def __init__(self):
        self.RepositoryAspirant = AspirantRepository()
        self.RepositoryParty = PartyRepository()

    def index(self):
        return self.RepositoryAspirant.findAll()

    def create(self, infoAspirant):
        newtheAspirantAspirant = Aspirant(infoAspirant)
        return self.RepositoryAspirant.save(newtheAspirantAspirant)
    def show(self, id):
        theAspirant = Aspirant(self.RepositoryAspirant.findById(id))
        return theAspirant.__dict__

    def update(self, id, infoAspirant):
        theAspirant = Aspirant(self.RepositoryAspirant.findById(id))
        theAspirant.cedula = infoAspirant["cedula"]
        theAspirant.numero_resolucion = infoAspirant["numero_resolucion"]
        theAspirant.nombre = infoAspirant["nombre"]
        theAspirant.apellido = infoAspirant["apellido"]
        return self.RepositoryAspirant.save(theAspirant)

    def delete(self, id):
        return self.RepositoryAspirant.delete(id)
    
    def assingAspirant(self, id, id_Party):
        AspirantCurrent = Aspirant(self.RepositoryAspirant.findById(id))
        PartyCurrent = Party(self.RepositoryParty.findById(id_Party))
        AspirantCurrent.Party = PartyCurrent
        return self.RepositoryAspirant.save(AspirantCurrent)

