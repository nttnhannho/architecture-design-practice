from abc import ABC, abstractmethod


class Search(ABC):
    @abstractmethod
    def search_by_title(self, title):
        pass

    @abstractmethod
    def search_by_author(self, author):
        pass

    @abstractmethod
    def search_by_subject(self, subject):
        pass

    @abstractmethod
    def search_by_pub_date(self, publish_date):
        pass
