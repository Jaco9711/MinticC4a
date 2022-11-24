from Repositories.InterfaceRepository import InterfaceRepository
from Models.Result import Result
from bson import ObjectId

class ResultRepository(InterfaceRepository[Result]):
    #Da las votaciones por Table
    def getListAspirantsinscribedTable(self, id_Table):
        theQuery = {"Table.$id": ObjectId(id_Table)}
        return self.query(theQuery)

    #Da las votaciones por Aspirant
    def getListTablesAspirantsigned(self, id_Aspirant):
        theQuery = {"Aspirant.$id": ObjectId(id_Aspirant)}
        return self.query(theQuery)

    # Numero mayor de una cédula
    def getNumeroCedulaMayorAspirant(self):
        query = {
            "$group":{
                "_id": "$Aspirant",
                "Total_votaciones_por_id": {
                    "$sum": 1
                },
                "doc": {
                    "$first": "$$ROOT"
                }
            }
        }
        pipeline = [query]
        return self.queryAggregation(pipeline)
