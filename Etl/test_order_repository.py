from entities.order import Order
from entities.book import Book
from entities.customer import Customer
from repositories.order_repository import OrderRepository
from datetime import date

def test_verify_order_id():

    #Arrange
    order_repository = OrderRepository()
    customer = Customer(1, "Kai")
    today = date.today()
    order = Order(1, customer, today)
 
    #Act
    order_repository.list_orders.append(order)
    resultado = order_repository.verify_order_id(1, order_repository)

    #Assert
    assert resultado == True

def test_verify_if_book_exists():

    #Arrange
    book = Book(1, "Calisto", "ttt", "Brtt", "Ação", 25.90)    
    list_books: list[Book] = []
    order_repository = OrderRepository()

    #Act
    list_books.append(book)
    resultado = order_repository.verif_if_book_exists(book.id, list_books)

    #Assert
    assert resultado == True

def test_verify_book_has_stock():

    #Arrange    
    order_repository = OrderRepository()
    book = Book(1, "Calisto", "ttt", "Brtt", "Ação", 25.90)
    book.stock = 1

    #act
    resultado = order_repository.verify_book_has_stock(book)

    #Assert
    assert resultado == True
    assert book.stock == 0