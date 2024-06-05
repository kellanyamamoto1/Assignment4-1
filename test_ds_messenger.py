import socket
import json
import time
from ds_messenger import DirectMessage, DirectMessenger
import Profile as p
import pathlib
server = "168.235.86.101"
port = 3021
timestamp = str(time.time())


def start():
    '''
    Start Function to Start Code
    '''
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_conn:
        server_conn.connect((server, port))
        stuff = {}
        stuff["join"] = {
                        "username": 'green1',
                        "password": 'heheha',
                        "token": ""
                    }
        data_str = json.dumps(stuff)
        server_conn.sendall(data_str.encode())
        response = server_conn.recv(3021).decode()
        response_json = json.loads(response)
        print(response_json)
        if "token" in str(response_json):
            temp = str(response_json).index("token")
            token = str(response_json)[temp+9:-3]
        mew = DirectMessenger("168.235.86.101", 'green1', 'heheha')
        person = p.Profile("168.235.86.101", 'green1', 'heheha')
        currrent_directory = pathlib.Path.cwd()
        path = f"{currrent_directory}\\profile.dsu"
        if not pathlib.Path(path).exists():
            with open(path, 'w') as file:
                person.save_profile(path)
        else:
            person.load_profile(path)
        mew.token = token
        print(mew.retrieve_all())
        temp = mew.retrieve_all()
        for i in temp:
            print(i.recipient)
        person.save_messages(mew.retrieve_all_string())
        # mew.send("cap111", 'help')
        person.save_sent(mew.send_format("test3", 'help'))
        person.save_profile(path)
        # person.load_sent()
        # person.del_messages()
        # person.del_sent()
        person.save_profile(path)


if __name__ == '__main__':
    '''
    Function to start code
    '''
    start()
