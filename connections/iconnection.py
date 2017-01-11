
from abc import ABCMeta, abstractmethod, abstractproperty


class IConnection(object, metaclass=ABCMeta):
    """
    Reference interface for Connection classes;
    inheritance is not necessary, though recommended
    """

    connection_types = {}
    url = None
    user = None
    password = None
    unique_id = None
    class_type = 'Base_class'

    def __init__(self, connection_url, username, passwrd, **kwargs):
        self.url = connection_url
        self.user = username
        self.password = passwrd

    @abstractmethod
    def geturl(self):
        """
        return the url.
        """
        return self.url

    @abstractmethod
    def getusername(self):
        return self.user

    @abstractmethod
    def getpassword(self):
        return self.password

    @abstractmethod
    def getproxy(self):
        raise NotImplementedError

    @abstractproperty
    def id(self):
        raise NotImplementedError

    @abstractproperty
    def classtype(self):
        return self.class_type
