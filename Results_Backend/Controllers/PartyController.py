from Repositories.PartyRepository import PartyRepository
from Models.Party import Party

class PartyController():
    
    def __init__(self):
        self.RepositoryParty = PartyRepository()
    
    def index(self):
        return self.RepositoryParty.findAll()
    
    def create(self, infoParty):
        newtheAspirantParty = Party(infoParty)
        return self.RepositoryParty.save(newtheAspirantParty)
    
    def show(self, id):
        elParty = Party(self.RepositoryParty.findById(id))
        return elParty.__dict__
    
    def update(self, id, infoParty):
        PartyCurrent = Party(self.RepositoryParty.findById(id))
        PartyCurrent.nombre = infoParty["nombre"]
        PartyCurrent.lema = infoParty["lema"]
        return self.RepositoryParty.save(PartyCurrent)
    
    def delete(self, id):
        return self.RepositoryParty.delete(id)
