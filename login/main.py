from getpass import getpass
from json import loads, dumps
from hashlib import sha256


def signin():
    login = input('Digite o seu login:\n> ')
    senha = getpass(prompt='Digite sua senha:\n> ')

    users = get_json()
    if login in users and users[login] == hashme(senha):
        print("Login bem-sucedido!")
    else:
        print("Credenciais incorretas!")


def get_json():
    with open('data/contas.json', 'r') as f:
        file = f.read()
    return loads(file)


def hashme(password: str):
    return sha256(password.encode()).hexdigest()


def set_json(json_data):
    with open('data/contas.json', 'w') as f:
        f.write(dumps(json_data))


def signup():
    new_login = input('Digite o seu nome de usuário:\n> ')
    new_pass = getpass(prompt='Digite sua melhor senha:\n> ')
    
    users = get_json()
    
    if new_login in users:
        print('Este usuário já existe!')
        return 

    users[new_login] = hashme(new_pass)
    set_json(users)
    print("Usuário cadastrado com sucesso!")

action = input("Deseja se cadastrar ou fazer login? (signup/signin): ").strip().lower()
if action == "signup":
    signup()
elif action == "signin":
    signin()
else:
    print("Ação inválida!.a")
