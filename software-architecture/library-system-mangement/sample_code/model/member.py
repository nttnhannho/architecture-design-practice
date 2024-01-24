from datetime import date
from account import Account
from account_status import AccountStatus


class Member(Account):
    def __init__(self, id_, password, person, status=AccountStatus.ACTIVE):
        super().__init__(id_, password, person, status)
        self.__date_of_membership = date.today()
        self.__total_books_checkout = 0

    @property
    def total_books_checkout(self):
        return self.__total_books_checkout

    def reserve_book_item(self):
        pass

    def increase_total_books_checked_out(self):
        pass

    def renew_book_item(self):
        pass

    def check_out_book_item(self):
        pass

    def check_for_fine(self):
        pass

    def return_book_item(self):
        pass
