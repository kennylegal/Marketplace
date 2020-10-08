from typing import List
from services.dto.customer_dto import CustomerUpdate, ListCustomers, CustomerDetails
from abc import abstractmethod,  ABCMeta
from services.models import *


class CustomerRepository(metaclass=ABCMeta):
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


class DjangoORMForCustomerRepository(CustomerRepository):
    def update(self, name: str, model: CustomerUpdate):
        try:
            customer = Customer.objects.get(name=name)
            customer.username = model.name
            customer.phone_no =model.phone_no
            customer.home_address = model.home_address
            customer.DOB = model.DOB
            customer.social_media = model.social_media
            customer.save()
        except Customer.DoesNotExist as error:
            print('Customer does not exist')
            raise error

    def list(self) -> List[ListCustomers]:
        customer = list(Customer.objects.values(
            'id',
            'name',
            'phone_no',
            'home_address'
        ))
        values: List[ListCustomers] = []
        for customers in customer:
            value = ListCustomers()
            value.id = customers['id']
            value.name = customers['name']
            value.phone_no = customers['phone_no']
            value.home_address = customers['home_address']
            values.append(value)
        return values

    def details(self, name: str) -> CustomerDetails:
        try:
            customer = Customer.objects.get(name=name)
            item = CustomerDetails()
            item.id = customer.id
            item.name = customer.name
            item.phone_no = customer.phone_no
            item.home_address = customer.home_address
            item.social_media = customer.social_media
            return item
        except Customer.DoesNotExist as error:
            print('customer does not exist')
            raise error

