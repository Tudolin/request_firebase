import requests
import json


create_userdata = {"id":"","name":"","lastname":"", "occupation":"" }

def cadastro():
    name = str(input("Insira seu nome = "))
    lastname = str(input("Insira seu sobrenome = "))
    occupation = str(input("Insira seu cargo = "))
    create_userdata['name'] = name
    create_userdata['lastname'] = lastname
    create_userdata['occupation'] = occupation


cadastro()

create_userdata_serial = json.dumps(create_userdata)


request = requests.post(url='https://teste-estudos-4706a-default-rtdb.firebaseio.com/.json', data=create_userdata_serial)
print(request)
print(request.json())