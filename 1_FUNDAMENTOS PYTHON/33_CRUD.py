import os
import csv

ARCHIVO_CLIENTE = '.clients.csv'  # Nombre del archivo de clientes
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []

def _initialize_clients_from_storage():
    print("Initializing")
    
    # Verifica si el archivo existe
    if not os.path.exists(ARCHIVO_CLIENTE):
        # Si no existe, crea el archivo vacío con las columnas definidas
        with open(ARCHIVO_CLIENTE, mode='w') as file:
            pass # Simplemente crea el archivo vacío
    
    # Ahora, abre el archivo para lectura
    with open(ARCHIVO_CLIENTE, mode='r') as file:
        reader = csv.DictReader(file, fieldnames=CLIENT_SCHEMA)
        for row in reader:
            clients.append(row)
        # El archivo se cierra automáticamente al salir del bloque 'with'


def _save_clients_to_storage():
    # tmp_table_name = '{}.tmp'.format(ARCHIVO_CLIENTE)  # .clients.csv.tmp
    guardado_temporal = './salida.csv' # .clients.csv.tmp
    with open(guardado_temporal, mode='w') as file:  # Usando tmp_table_name correctamente
        writer = csv.DictWriter(file, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

    os.remove(ARCHIVO_CLIENTE)  # Eliminamos la tabla original
    os.rename(guardado_temporal, ARCHIVO_CLIENTE)  # Renombramos la tabla temporal

    # El archivo se cierra automáticamente al salir del bloque 'with'


def create_client(client):# Habrá que pasar un diccionario o la llave
    global clients
    if client not in clients:
        clients.append(client)
    else:
        print('Client already in client\'s list')


def list_clients():
    print('id |  name  | company  | email  | position ')
    print('*' * 50)
    for idx, client in enumerate(clients):
        print(' {uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx, 
            name=client['name'], 
            company=client['company'], 
            email=client['email'], 
            position=client['position']))


def update_client(client_id, updated_client):
    global clients

    if len(clients) - 1 >= client_id:
        clients[client_id] = updated_client
    else:
        print('Client not in client\'s list')


def delete_client(client_id):
    global clients
    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx] 
            break


def search_client(client_name):
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True

# Excelente
def _get_client_field(field_name, message='What is the client {}?'):
    field = None
    while not field:
        field = input(message.format(field_name))
    return field


def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }

    return client


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?:')
    print('[C]reate client')
    print('[L]ist clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')


if __name__ == '__main__':
    _initialize_clients_from_storage()

    _print_welcome()

    command = input()
    command = command.upper()

    if   command == 'C':
        client = _get_client_from_user()
        create_client(client)
        

    elif command == 'L':
        list_clients()

    elif command == 'U':
        client_id = int(_get_client_field('id'))
        updated_client = _get_client_from_user()
        update_client(client_id, updated_client)

    elif command == 'D':
        client_id = int(_get_client_field('id'))
        delete_client(client_id)

    elif command == 'S':
        client_name = _get_client_field('name')
        print("Client name: %s," % client_name, "Searching . . .")
        found = search_client(client_name)        
        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))

    else:
        print('Invalid command')

    _save_clients_to_storage()