# Verificar se o estoque do livro foi baixado ------------
# Não permitir inserir um código de cliente que já existe ------------
# Não permitir inserir um código de pedido que já existe -------------
# Não permitir vender um livro com valor zerado  -----------------
# Não permitir fazer um pedido sem cliente ---------------
# Não permitir um pedido sem livro 
# Só é permitido informar UM pedido no pedido 
# Caso o formato do valor do esteja errado retornar 0
# Não permitir vender o mesmo livro novamente, pois a livraria só possui 1 estoque --------------------
# Verificar se o código do livro que está sendo vendido, existe, caso não exista aborta o pedido e volta para o menu ------------

from datetime import date

from entities.book import Book
from entities.customer import Customer
from entities.order import Order
from repositories.customer_repository import CustomerRepository
from repositories.order_repository import OrderRepository

file_book = list(open("books.csv", "r", encoding="utf-8"))

list_books: list[Book] = []

def format_str_price_to_float(price: str) -> float:
    try:
        return float(price.replace("R$ ", "").replace(",", "."))
    except:
        return 0


def principal_menu() -> int:
    try:
        print("1 - Cadastrar cliente")
        print("2 - Fazer pedido")
        print("3 - Relatório de Pedidos")
        print("4 - Relatório de Clientes")
        print("5 - Relatório de Livros")
        print("0 - Sair")
        return int(input("Informe a opção do menu: "))
    except:
        print("A opção informada é inválida, o programa vai ser encerrado...")
        return 0


for book in file_book[1:]:
    list_book = book.split(";")
    book = Book(int(list_book[0]), list_book[1], list_book[2], list_book[3],
                list_book[4], format_str_price_to_float(list_book[5]))
    list_books.append(book)

customer_repository = CustomerRepository()
order_repository = OrderRepository()

while True:
    menu_option = principal_menu()
    if (menu_option == 0):
        break

    print("\n")

    if menu_option == 1:
        id = int(input("Informe o código do cliente: "))
        if (customer_repository.verify_customer_id(id, customer_repository)):
            print("Esse id de cliente já existe!\n")
        else:    
            nome = input("Informe o nome do cliente: ")
            customer = Customer(id, nome)
            customer_repository.list_customers.append(customer)
            print("Client cadastrado com sucesso!\n")

    if menu_option == 2:
        try:
            id = int(input("Informe o código do pedido: "))   
            if order_repository.verify_order_id(id, order_repository):
                print("Esse código de pedido já existe ou código informado vazio!\n")
        except:
                print("Código informado vazio!")

        else: 
            try:
                customer_id = int(input("Informe o código do cliente: "))
                today = date.today()
                if (not customer_repository.verify_if_customer_exists(customer_id, customer_repository)):
                    print("Cliente não existe!\n")
                    continue
            except:
                print("Não é possivel fazer um pedido sem cliente!")
                customer_id = -1
                today = date.today()

            customer = customer_repository.get_customer(customer_id, customer_repository)
            book_id = int(input("Informe o código do livro: "))

            if (not order_repository.verif_if_book_exists(book_id, list_books)):
                print("Livro não existe!\n")
                continue

            book = order_repository.get_book(book_id, list_books)
            if order_repository.verify_book_has_stock(book):
                order = Order(id, customer, today)
                order.purchased_book = book

                order_repository.list_orders.append(order)
                print("Pedido cadastrado com sucesso!")
            else:    
                print("Não existe estoque disponível para este livro!")    

    if menu_option == 3:
        print("\n***** Relatório de pedidos *****\n")
        for order in order_repository.list_orders:
            print(f"Código do Pedido: {order.id}")
            print(f"Cliente: {order.customer.name}")
            print(f"Data do pedido: {order.date_order}")
            print(f"Livro escolhido: {order.purchased_book.name} \n")

    if menu_option == 4:
        formatText = "{0:<10} {1:<20}\n"
        menu = ("\n***** Relatório de clientes *****\n")
        menu += formatText.format("Id", "Cliente")

        for customer in customer_repository.list_customers:
            menu += formatText.format(customer.id, customer.name)
        print(menu)

    if menu_option == 5:
        formatText = "{0:<10} {1:<20} {1:<20} {1:<20} {1:<20} {1:<20}\n"
        menu = ("\n***** Relatório de livros cadastrados *****\n")
        menu += formatText.format("Id", "Ttítulo", "ISBN",
                                  "Autor", "Assunto", "Valor", "Estoque")

        for book in list_books:
            menu += formatText.format(book.id, book.name, book.isbn,
                                      book.author, book.category, book.price, book.stock)
        print(menu)
