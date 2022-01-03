from abc import ABC, abstractmethod
from account_status import AccountStatus


class Account(ABC):
    def __init__(self, id_, password, person, status=AccountStatus.ACTIVE):
        self.__id = id_
        self.__password = password
        self.__person = person
        self.__status = status

    def reset_password(self):
        pass
