from account import Account
from account_status import AccountStatus


class Librarian(Account):
    def __init__(self, id_, password, person, status=AccountStatus.ACTIVE):
        super().__init__(id_, password, person, status)

    def add_book_item(self):
        pass

    def block_member(self):
        pass

    def unblock_member(self):
        pass
