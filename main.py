import sys
import os
import csv


CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []
command = True


def _initialice_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)


def _save_clients_to_storage():
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

        os.remove(CLIENT_TABLE)
        os.rename(tmp_table_name, CLIENT_TABLE)



def create_clients(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already is in the client\'s list')


def search_client(client_name):
    
    for client in clients:
        if client['name'] != client_name:
            return False
        else:
            return True


def list_clients():
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']))
        print('*' * 50)

def update_client(idx, updated_client_name):
    global clients

    clients[idx]['name'] = updated_client_name


def delete_client(client_idx):
    global clients
    
    del clients[client_idx]


def _add_comma():
    global clients

    clients += ','

def _print_welcome():
    print(' ' * 50)
    print(' ' * 50)
    print('WELCOME TO ADMIN CLIENT')
    print('*' * 50)
    print('what would you like today')
    print('(C)reate client')
    print('(U)pdate client')
    print('(D)elete client')
    print('(S)earch client')
    print('(L)ist client')
    print('(E)xit')
    




def _get_client_field(field_name):
    field = None

    while not field:
        field = input('What is the client {}: '.format(field_name))

    return field


def _get_client_idx(client_name):
    state = None

    for idx, client in enumerate(clients):

        if client['name'] == client_name:
            state = idx
            print(idx)

    return state


def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name: ')

        if client_name == 'exit':
            client_name == None
            break

    if not client_name:
        sys.exit()

    return client_name.lower()


if __name__ == '__main__':
    _initialice_clients_from_storage()
    while command:        
        _print_welcome()
    
        command = input()
        command = command.upper()

        if command == 'C':
            client ={
            'name': _get_client_field('name'),
            'company' : _get_client_field('company'),
            'email' : _get_client_field('email'),
            'position' : _get_client_field('position')
        }
            create_clients(client)
        elif command == 'D':
            client_name = _get_client_name()
            client_idx = _get_client_idx(client_name)

            if client_idx is None:
                print('sorry, the client not exists')
                print('*'*50)
            else:        
                delete_client(client_idx) 
        elif command == 'U':
            client_name = _get_client_name()
            updated_client_name = input('What is the updated client name: ')
            client_idx = _get_client_idx(client_name)
            if client_idx is  None:
                print('We are sorry, the client doesn\'t exists')
            else:
                update_client(client_idx, updated_client_name)
        elif command == 'S':
            client_name = _get_client_name()
            found = search_client(client_name)
            
            if search_client is False:
                print('The client is in the client\'s list')
            else:
                print('The client: {} is not un client\'s list'.format(client_name))
        elif command == 'L':
            list_clients()
        elif command == 'E':
            command = False
            print('Session endend')
            os.system('clear')
            
        else:
            print('Invalid command')
        _save_clients_to_storage()

