class BookLending:
    def __init__(self, creation_date, due_date, book_item_barcode, member_id):
        self.__creation_date = creation_date
        self.__due_date = due_date
        self.__return_date = None
        self.__book_item_barcode = book_item_barcode
        self.__member_id = member_id

    @staticmethod
    def lend_book(barcode):
        pass

    def fetch_lending_details(self, barcode):
        pass
