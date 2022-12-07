

from entities.customer import Customer


class CustomerRepository:
    def __init__(self) -> None:
        self.list_customers: list[Customer] = []

    def verify_if_customer_exists(self, customer_id: int, CustomerRepository) -> bool:
        for customer in CustomerRepository.list_customers:
            if (customer.id == customer_id):
                return True

        return False
            

    def get_customer(self, customer_id: int, CustomerRepository) -> Customer:
        for customer in CustomerRepository.list_customers:
            if (customer.id == customer_id):
                return customer

        return Customer(-1, "Client not found!")

    def verify_customer_id(self, customer_id: int, CustumerRepository) -> bool:
        for customer in CustumerRepository.list_customers:
            if (customer.id == customer_id):
                return True
        return False        
    