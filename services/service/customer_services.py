from services.dto.customer_dto import CustomerDetails, CustomerUpdate, ListCustomers
from services.repositories.customer_repository import *
from abc import ABCMeta, abstractmethod
from typing import List


class CustomerServices(metaclass=ABCMeta):
    @abstractmethod
    def update(self, name: str, model: CustomerUpdate):
        """updates a customer object"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListCustomers]:
        """List all available Customers"""
        raise NotImplementedError

    @abstractmethod
    def details(self, name: str) -> CustomerDetails:
        """Gets the details of a customer"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, name: str):
        """deletes a customer"""
        raise NotImplementedError


class DefaultDjangoServicesForCustomer(CustomerServices):
    repository: CustomerRepository = None

    def __init__(self, repository: CustomerRepository):
        self.repository = repository

    def update(self, name: str, model: CustomerUpdate):
        self.repository.update(name, model)

    def list(self) -> List[ListCustomers]:
        return self.repository.list()

    def details(self, name: str) -> CustomerDetails:
        return self.repository.details(name)

    def delete(self, name: str):
        return self.repository.delete(name)