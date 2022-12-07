from entities.customer import Customer
from repositories.customer_repository import CustomerRepository

def test_verify_if_customer_exists():

    #Arrange
    customer_repository = CustomerRepository()
    custumer = Customer(1, "Kaique")
    customer_repository.list_customers.append(custumer)

    #Act 
    resultado = customer_repository.verify_if_customer_exists(1, customer_repository)

    #Assert
    assert resultado == True
 