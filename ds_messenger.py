import socket
import json
import time
from ds_protocol import format_for_json
server = "168.235.86.101"
port = 3021
timestamp = str(time.time())


class DirectMessage:

    def __init__(self):
        self.recipient = None
        self.message = None
        self.timestamp = None


class DirectMessenger:
    def __init__(self, dsuserver=None, username=None, password=None):
        self.token = None
        self.dsuserver = dsuserver
        self.username = username
        self.password = password

    def connect(self):
        '''
        Function to Connect
        '''
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_conn:
            server_conn.connect((self.dsuserver, port))
            stuff = {}
            stuff["join"] = {
                            "username": 'ke',
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
                self.token = token

    def send(self, message: str, recipient: str) -> bool:
        if self.token is None:
            self.connect()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_conn:
            server_conn.connect((self.dsuserver, port))
            action = '1'
            formated = format_for_json(action, user_token=self.token,
                                       message=message, recipient=recipient)
            data_str = json.dumps(formated)
            server_conn.sendall(data_str.encode())
            response = server_conn.recv(3021).decode()
            response_json = json.loads(response)
            print(response_json)
            print(data_str)
            if "response" in response_json:
                if response_json["response"]["type"] == "ok":
                    return True
                else:
                    error_message = response_json["response"]["message"]
                    print("Error:", error_message)
                    return False
            else:
                print("Invalid response from server")
                return False

    def send_format(self, message: str, recipient: str) -> bool:
        formated = ({
            "token": self.token,
            "directmessage": {
                    "entry": message,
                    "recipient": recipient,
                    'timestamp': timestamp
                    }
        })
        data_str = formated
        return (data_str)

    def retrieve_new(self) -> list:
        '''
        Function to retrieve new messages
        '''
        messages = []
        if self.token is None:
            self.connect()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_conn:
            server_conn.connect((self.dsuserver, port))
            action = '2'
            formated = format_for_json(action, self.token)

            data_str = json.dumps(formated)
            server_conn.sendall(data_str.encode())
            response = server_conn.recv(3021).decode()
            response_json = json.loads(response)
            if "response" in response_json:
                if response_json["response"]["type"] == "ok":
                    msg_list = response_json['response']['messages']
                    print(msg_list)
                    for msg in msg_list:
                        msg_object = DirectMessage()
                        msg_object.recipient = msg['from']
                        msg_object.message = msg['message']
                        msg_object.timestamp = msg['timestamp']
                        messages.append(msg_object)

                else:
                    error_message = response_json["response"]["message"]
                    print("Error:", error_message)
            else:
                print("Invalid response from server")
        return messages

    def retrieve_all(self) -> list:
        messages = []
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_conn:
            server_conn.connect((self.dsuserver, port))
            formated = {
                "token": self.token,
                "directmessage": 'all'
            }

            data_str = json.dumps(formated)
            server_conn.sendall(data_str.encode())

        # Receive the entire message at once
            response = server_conn.recv(3021).decode()
            print("Response:", response)  # Print the response to debug

            try:
                response_json = json.loads(response)
                if "response" in response_json:
                    if response_json["response"]["type"] == "ok":
                        msg_list = response_json['response']['messages']
                        for msg in msg_list:
                            print(msg)
                            msg_object = DirectMessage()
                            msg_object.recipient = msg['from']
                            msg_object.message = msg['message']
                            msg_object.timestamp = msg['timestamp']
                            messages.append(msg_object)

                    else:
                        error_message = response_json["response"]["message"]
                        print("Error:", error_message)
                else:
                    print("Invalid response from server")
            except json.decoder.JSONDecodeError as e:
                print("Error decoding JSON:", e)

        return messages

    def retrieve_all_string(self) -> list:
        messages = []
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_conn:
            server_conn.connect((self.dsuserver, port))
            formated = ({
                "token": self.token,
                "directmessage": 'all'
            })

            data_str = json.dumps(formated)
            server_conn.sendall(data_str.encode())
            response = server_conn.recv(3021).decode()
            response_json = json.loads(response)
            if "response" in response_json:
                if response_json["response"]["type"] == "ok":
                    msg_list = response_json['response']['messages']
                    for msg in msg_list:
                        messages.append(msg)

                else:
                    error_message = response_json["response"]["message"]
                    print("Error:", error_message)
            else:
                print("Invalid response from server")
        return messages

    def return_user(self):
        return self.username

    def return_pass(self):
        return self.password