from flask import Flask, jsonify, request
from flask_cors import CORS
from waitress import serve
import datetime
import requests
import re
import json

app = Flask(__name__)
cors = CORS(app)

######################################
##         Librerias JWT            ##
######################################
from flask_jwt_extended import create_access_token, verify_jwt_in_request
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

######################################
##            CREAR TOKEN           ##
######################################
app.config["JWT_SECRET_KEY"] = 'super-secret' #puedes colocar la que quieras
jwt = JWTManager(app)


@app.route("/login", methods=['POST'])
def create_token():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-security"]+"/usuarios/validar"
    response = requests.post(url, json= data, headers=headers)
    if response.status_code == 200:
        user = response.json()
        expires = datetime.timedelta(seconds=60*60*24)
        access_token = create_access_token(identity=user,
            expires_delta=expires)
        return jsonify({"token": access_token,
            "user_id": user["_id"]})
    else:
        return jsonify({
            "Message": "correo o contraseña invalidos. "
        }), 401

######################################
##            MIDDLEWARE            ##
######################################
def limpiarURL(url):
    partes = request.path.split("/")
    for laParte in partes:
        if re.search('\\d', laParte):
            url = url.replace(laParte, "?")
    return url

def validarPermiso(endPoint, metodo, idRol):
    url = dataConfig["url-backend-security"]+ "/permisos-roles/validar-permiso/rol/"+str(idRol)
    tienePermiso= False
    headers = {"Content-Type": "application/json; charset=utf-8"}
    body = {
        "url": endPoint,
        "metodo": metodo
    }
    response = requests.get(url, json=body, headers=headers)
    try: 
        data = response.json()
        if("_id" in data):
            tienePermiso = True
    except:
        pass
    return tienePermiso

@app.before_request
def before_request_callback():
    endPoint = limpiarURL(request.path)
    excludedRoutes = ["/login"]
    if excludedRoutes.__contains__(request.path):
        print("ruta excluida ", request.path)
        pass
    elif verify_jwt_in_request():
        usuario = get_jwt_identity()
        if usuario["rol"] is not None:
            tienePermiso =  validarPermiso(endPoint,
                request.method, usuario["rol"]["_id"])
            if not tienePermiso:
                return jsonify({
                    "message ": "usted no tiene permisos"
                }), 401
        else:
            return jsonify({
                    "message ": "usted no es el usuario o verifiquelo"
                }), 401

####################################
##        ENDPOINTS DE Tables      ##
####################################
@app.route("/Tables", methods=["GET"])
def getTables():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-votes"]+'/Tables'
    response = requests.get(url, headers=headers)
    Json = response.json()
    return jsonify(Json)

@app.route("/Tables", methods=["POST"])
def crearTable():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-votes"]+'/Tables'
    response = requests.post(url, headers=headers, json=data)
    Json = response.json()
    return jsonify(Json)

@app.route("/Tables/<string:id>", methods=["GET"])
def getTable(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-votes"]+'/Tables/'+id
    response = requests.get(url, headers=headers)
    Json = response.json()
    return jsonify(Json)

@app.route("/Tables/<string:id>", methods=["PUT"])
def modificarTable(id):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-votes"]+'/Tables/'+id
    response = requests.put(url, headers=headers, json=data)
    Json = response.json()
    return jsonify(Json)

@app.route("/Tables/<string:id>", methods=["DELETE"])
def deleteTable(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-votes"]+'/Tables/'+id
    response = requests.delete(url, headers=headers)
    Json = response.json()
    return jsonify(Json)

####################################
##     ENDPOINTS DE Parties      ##
####################################
@app.route("/Parties", methods=["GET"])
def getParties():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-votes"]+'/Parties'
    response = requests.get(url, headers=headers)
    Json = response.json()
    return jsonify(Json)

@app.route("/Parties", methods=["POST"])
def crearParty():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-votes"]+'/Parties'
    response = requests.post(url, headers=headers, json=data)
    Json = response.json()
    return jsonify(Json)

@app.route("/Parties/<string:id>", methods=["GET"])
def getParty(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-votes"]+'/Parties/'+id
    response = requests.get(url, headers=headers)
    Json = response.json()
    return jsonify(Json)

@app.route("/Parties/<string:id>", methods=["PUT"])
def modificarParty(id):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-votes"]+'/Parties/'+id
    response = requests.put(url, headers=headers, json=data)
    Json = response.json()
    return jsonify(Json)

@app.route("/Parties/<string:id>", methods=["DELETE"])
def deleteParty(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-votes"]+'/Parties/'+id
    response = requests.delete(url, headers=headers)
    Json = response.json()
    return jsonify(Json)

####################################
##   ENDPOINTS DE Aspirants      ##
####################################
@app.route("/Aspirants", methods=["GET"])
def getAspirants():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-votes"]+'/Aspirants'
    response = requests.get(url, headers=headers)
    Json = response.json()
    return jsonify(Json)

@app.route("/Aspirants", methods=["POST"])
def crearAspirant():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-votes"]+'/Aspirants'
    response = requests.post(url, headers=headers, json=data)
    Json = response.json()
    return jsonify(Json) 

@app.route("/Aspirants/<string:id>", methods=["GET"])
def getAspirant(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-votes"]+'/Aspirants/'+id
    response = requests.get(url, headers=headers)
    Json = response.json()
    return jsonify(Json)

@app.route("/Aspirants/<string:id>", methods=["PUT"])
def modificarAspirant(id):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-votes"]+'/Aspirants/'+id
    response = requests.put(url, headers=headers, json=data)
    Json = response.json()
    return jsonify(Json)

@app.route("/Aspirants/<string:id>", methods=["DELETE"])
def deleteAspirant(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-votes"]+'/Aspirants/'+id
    response = requests.delete(url, headers=headers)
    Json = response.json()
    return jsonify(Json)

@app.route("/Aspirants/<string:id_Aspirant>/Party/<string:id_Party>", methods=["PUT"])
def asignarAspirant(id_Aspirant, id_Party):
    data = {
        "Aspirant":{},
        "Party": {}
    }
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-votes"]+"/Aspirants/"+id_Aspirant+"/Party/"+ id_Party
    response = requests.put(url, headers=headers, json= data)
    Json = response.json()
    return jsonify(Json)


####################################
##   ENDPOINTS DE Results      ##
####################################
@app.route("/Results", methods=["GET"])
def getResults():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-votes"]+'/Results'
    response = requests.get(url, headers=headers)
    Json = response.json()
    return jsonify(Json)

@app.route("/Results/Table/<string:id_Table>/Aspirant/<string:id_Aspirant>", methods =["POST"])
def crearResult(id_Table, id_Aspirant):
    data = {}
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-votes"]+"/Results/Table/"+id_Table+"/Aspirant/"+id_Aspirant
    response = requests.post(url, headers=headers, json=data)
    Json = response.json()
    return jsonify(Json)


@app.route("/Results/<string:id>", methods=["GET"])
def getResult(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-votes"]+'/Results/'+id
    response = requests.get(url, headers=headers)
    Json = response.json()
    return jsonify(Json)

@app.route("/Results/<string:id_Result>/Table/<string:id_Table>/Aspirant/<string:id_Aspirant>", methods=["PUT"])
def modificarResult(id_Result, id_Table, id_Aspirant):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-votes"]+"/Results/"+id_Result+"/Table/"+id_Table+"/Aspirant/"+id_Aspirant
    response = requests.put(url, headers=headers)
    Json = response.json()
    return jsonify(Json)

@app.route("/Results/<string:id>", methods=["DELETE"])
def deleteResult(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-votes"]+'/Results/'+id
    response = requests.delete(url, headers=headers)
    Json = response.json()
    return jsonify(Json)

#Mirar los Results de una Table en particular
@app.route("/Results/Table/<string:id_Table>", methods=["GET"])
def votosEnTable(id_Table):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-votes"]+'/Results/Table/'+id_Table
    response = requests.get(url, headers=headers)
    Json = response.json()
    return jsonify(Json)

#Mirar los votos de un Aspirant en todas las Tables
@app.route("/Results/Tables/<string:id_Aspirant>", methods=["GET"])
def votosAspirant(id_Aspirant):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-votes"]+'/Results/Tables/'+id_Aspirant
    response = requests.get(url, headers=headers)
    Json = response.json()
    return jsonify(Json)

#Conteo de los votos
@app.route("/Results/maxdocument", methods=["GET"])
def getConteoVotos():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-votes"]+'/Results/maxdocument'
    response = requests.get(url, headers=headers)
    Json = response.json()
    return jsonify(Json)

####################################
##   TEST O PRUEBA DEL SERVICIO   ##
####################################
@app.route("/", methods=['GET'])
def test():
    Json = {}
    Json["Message"]= "Server Running Working..."
    return jsonify(Json)

####################################
##             CONEXIÓN           ##
####################################
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == "__main__":
    dataConfig = loadFileConfig()
    print("Server url-backend running : http://"+
        dataConfig["url-backend"]+":"+
        dataConfig["port"])
    serve(app, host= dataConfig["url-backend"],
        port=dataConfig["port"])
        