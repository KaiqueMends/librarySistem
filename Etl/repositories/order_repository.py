from entities.order import Order
from entities.book import Book


class OrderRepository:
    def __init__(self) -> None:
        self.list_orders: list[Order] = []

    def verif_if_book_exists(self, book_id: int, list_books: list[Book]) -> bool:
        for book in list_books:
            if (book.id == book_id):
                return True

        return False


    def get_book(self, book_id: int,  list_books: list[Book]):
        for book in list_books:
            if (book.id == book_id):
                return book

        return Book(-1, "Book not found!", "", "", "", 0)

    def verify_order_id(self, order_id: int, OrderRepository) -> bool:
        if (order_id == ''):
            return False
        for order in OrderRepository.list_orders:
            if (order.id == order_id):
                return True
        return False 

    def verify_book_has_stock(self, Book) -> bool:
        if Book.stock > 0:
            Book.stock -= 1
            return True
        return False
            
