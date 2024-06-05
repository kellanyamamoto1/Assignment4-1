import json
import time
from pathlib import Path


"""
DsuFileError is a custom exception handler
that you should catch in your own code. It
is raised when attempting to load or save
Profile objects to file the system.

"""


class DsuFileError(Exception):
    pass


"""
DsuProfileError is a custom exception handler
that you should catch in your own code. It
is raised when attempting to deserialize a
dsu file to a Profile object.

"""


class DsuProfileError(Exception):
    pass


class Post(dict):
    """
    The Post class is responsible for working
    with individual user posts. It currently
    supports two features: A timestamp property
    that is set upon instantiation and
    when the entry object is set and an entry
    property that stores the post message.

    """
    def __init__(self, entry: str = None, timestamp: float = 0):
        self._timestamp = timestamp
        self.set_entry(entry)

        # Subclass dict to expose Post properties for serialization
        # Don't worry about this!
        dict.__init__(self, entry=self._entry, timestamp=self._timestamp)

    def set_entry(self, entry):
        self._entry = entry
        dict.__setitem__(self, 'entry', entry)

        # If timestamp has not been set, generate a new from time module
        if self._timestamp == 0:
            self._timestamp = time.time()

    def get_entry(self):
        return self._entry

    def set_time(self, time: float):
        self._timestamp = time
        dict.__setitem__(self, 'timestamp', time)

    def get_time(self):
        return self._timestamp

    """

    The property method is used to support
    get and set capability for entry and
    time values. When the value for entry
    is changed, or set, the timestamp field is
    updated to the current time.

    """
    entry = property(get_entry, set_entry)
    timestamp = property(get_time, set_time)


class Profile:

    def __init__(self, dsuserver=None, username=None, password=None, ):
        self.dsuserver = dsuserver  # REQUIRED
        self.username = username  # REQUIRED
        self.password = password  # REQUIRED
        self.received_messages = []
        self.sent_messages = []

    def del_messages(self):
        self.received_messages.clear()

    def save_messages(self, dict1):
        for i in dict1:
            self.received_messages.append(i)

    def load_messages(self):
        for i in self.received_messages:
            print(i)

    def save_sent(self, message):
        self.sent_messages.append(message)

    def load_sent(self):
        for i in self.sent_messages:
            print(i)

    def del_sent(self):
        self.sent_messages.clear()

    def save_profile(self, path: str) -> None:
        p = Path(path)
        if p.exists() and p.suffix == '.dsu':
            try:
                profile_data = {
                    'username': self.username,
                    'password': self.password,
                    'dsuserver': self.dsuserver,
                    'received_messages': self.received_messages,
                    'sent_messages': self.sent_messages
                }
                f = open(p, 'w')
                json.dump(profile_data, f)
                f.close()
            except Exception as ex:
                raise DsuFileError("Error while attempting"
                                   "to process the DSU file.", ex)
        else:
            raise DsuFileError("Invalid DSU file path or type")

    def load_profile(self, path: str) -> None:
        p = Path(path)
        if p.exists() and p.suffix == '.dsu':
            try:
                f = open(p, 'r')
                obj = json.load(f)
                self.username = obj['username']
                self.password = obj['password']
                self.dsuserver = obj['dsuserver']
                self.received_messages = obj['received_messages']
                self.sent_messages = obj['sent_messages']
                f.close()
            except Exception as ex:
                raise DsuProfileError(ex)
        else:
            raise DsuFileError()