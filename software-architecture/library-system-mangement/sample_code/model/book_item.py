from book import Book


class BookItem(Book):
    def __init__(self, ISBN, title, subject, publisher, language, number_of_pages,
                 barcode, is_reference_only, borrowed, due_date, price, book_format,
                 status, date_of_purchase, publication_date, placed_at):
        super().__init__(ISBN, title, subject, publisher, language, number_of_pages)
        self.__barcode = barcode
        self.__is_reference_only = is_reference_only
        self.__borrowed = borrowed
        self.__due_date = due_date
        self.__price = price
        self.__format = book_format
        self.__status = status
        self.__date_of_purchase = date_of_purchase
        self.__publication_date = publication_date
        self.__placed_at = placed_at

    @property
    def barcode(self):
        return self.__barcode

    @property
    def is_reference_only(self):
        return self.__is_reference_only

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    def check_out(self):
        pass
