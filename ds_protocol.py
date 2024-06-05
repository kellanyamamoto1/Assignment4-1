'''
Modified given file to connect to server
'''
# ds_protocol.py

# Starter code for assignment 3 in ICS 32 Programming with Software
# Libraries in Python

# Replace the following placeholders with your information.

# Kellan Yamamoto
# kellany@uci.edu
# 28388886


import test_ds_message_protocol
import json
import time
from collections import namedtuple
timestamp = str(time.time())
DataTuple = namedtuple('DataTuple', ['type', 'message'])


def json_to_dict(json_msg: str) -> dict:
    """
    Convert a JSON message to a dictionary.
    """
    try:
        return json.loads(json_msg)
    except json.JSONDecodeError:
        print("Json cannot be decoded.1")
        return {}


def json_to_list(json_msg: str) -> list:
    """
    Convert a JSON message to a list.
    """
    try:
        return json.loads(json_msg)
    except json.JSONDecodeError:
        print("Json cannot be decoded.2")
        return []


def extract_json(json_msg: str) -> DataTuple:
    '''
    Call the json.loads function on a
    json string and convert it to a DataTuple object
    '''
    try:
        json_obj = json.loads(json_msg)
        response = json_obj.get('response', {})
        if 'type' in response and 'message' in response:
            return DataTuple(response['type'], response['message'])
    except json.JSONDecodeError:
        print("Json cannot be decoded.3")

    return None


def format_for_json(action_type, user_token=None,
                    message=None, recipient=None):
    '''
    Function to format strings
    '''
    formated = None
    if action_type == "1":
        formated = ({
                "token": user_token,
                "directmessage": {
                    "entry": message,
                    "recipient": recipient,
                    'timestamp': timestamp
                }
                })
    elif action_type == '2':
        if not user_token:
            raise ValueError("no user token breh go get that shi")
        formated = ({
                "token": user_token,
                "directmessage": 'new'
                })
    elif action_type == '3':
        if not user_token:
            raise ValueError("go get it bruh bruh")
        formated = ({
                "token": user_token,
                "directmessage": 'all'
                })
    return formated