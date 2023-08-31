import requests
import json

#
class AutoIncrementID:
    def __init__(self):
        self.load_last_id()

    def load_last_id(self):
        try:
            with open("last_id.txt", "r") as file:
                self.current_id = int(file.read().strip())
        except FileNotFoundError:
            self.current_id = 1

    def save_last_id(self):
        with open("last_id.txt", "w") as file:
            file.write(str(self.current_id))

    def generate_id(self):
        new_id = self.current_id
        self.current_id += 1
        self.save_last_id()
        return new_id
    
id_generator = AutoIncrementID()

def cadastro(id_generator):

    create_userdata = {"id": id_generator.generate_id(),"name":"","lastname":"", "occupation":"" }

    name = str(input("Insira seu nome = "))
    lastname = str(input("Insira seu sobrenome = "))
    occupation = str(input("Insira seu cargo = "))
    create_userdata['name'] = name
    create_userdata['lastname'] = lastname
    create_userdata['occupation'] = occupation

    create_userdata_serial = json.dumps(create_userdata)

    request = requests.post(url='https://teste-estudos-4706a-default-rtdb.firebaseio.com/.json', data=create_userdata_serial)
    print(request)
    print(request.json())

cadastro(id_generator)

lista = json.load()


