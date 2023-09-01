import requests
import json

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
    while True:
        user_id = id_generator.generate_id()

        create_userdata = {
            "id": user_id,
            "name": "",
            "lastname": "",
            "occupation": ""
        }

        name = str(input("Insira seu nome = "))
        lastname = str(input("Insira seu sobrenome = "))
        occupation = str(input("Insira seu cargo = "))

        create_userdata['name'] = name
        create_userdata['lastname'] = lastname
        create_userdata['occupation'] = occupation

        create_userdata_serial = json.dumps(create_userdata)

        response = requests.put(f'"SEU URL AQUI"/user-data/{user_id}.json', data=create_userdata_serial)

        if response.status_code == 200:
            print(f"Cadastro realizado com sucesso! ID local gerado: {user_id}")
        else:
            print(f'Erro ao cadastrar: código de status {response.status_code}')

        continuar = input("Deseja continuar cadastrando? (s/n): ").strip().lower()
        if continuar != 's':
            break

def check_by_id():
    while True:
        id_a_procurar = str(input("Digite o ID que deseja procurar (ou 'q' para sair): ").strip().lower())
        
        if id_a_procurar == 'q':
            break
        
        url = f'"SEU URL AQUI"/user-data/{id_a_procurar}.json'
        response = requests.get(url, verify=False)  # Desativa a verificação do certificado SSL, sim, não é seguro, mas é para testes então tudo ok

        if response.status_code == 200:
            data = response.json()
            if data is not None:
                name = data.get('name')
                if name:
                    print(f"Nome encontrado para o ID '{id_a_procurar}': {name}")
                else:
                    print(f"Nome não encontrado para o ID '{id_a_procurar}'")
            else:
                print(f"ID '{id_a_procurar}' não encontrado no banco de dados")
        else:
            print(f'A solicitação falhou com o código de status {response.status_code}')

cadastro(id_generator)

check_by_id()
