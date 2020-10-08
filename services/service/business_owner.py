from abc import ABCMeta, abstractmethod
from services.dto.business_dto import BusinessUpdateDto, ListBusinessOwner, BusinessOwnerDetail
from typing import List
from services.repositories.b_o_repositories import BusinessRepository


class BusinessService(metaclass=ABCMeta):

    @abstractmethod
    def update(self, id: int, model: BusinessUpdateDto):
        """updates a customer object"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListBusinessOwner]:
        """list all available business owners"""
        raise NotImplementedError

    @abstractmethod
    def details(self, id: int) -> BusinessOwnerDetail:
        """shows the details of a business owner"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, business_user: str):
        """deletes a business owner"""
        raise NotImplementedError


class DefaultOwnerServices(BusinessService):
    repository: BusinessRepository = None

    def __init__(self, repository: BusinessRepository):
        self.repository = repository

    def update(self, id: int, model: BusinessUpdateDto):
        return self.repository.update(id, model)

    def list(self) -> List[ListBusinessOwner]:
        return self.repository.list()

    def details(self, id: int) -> BusinessOwnerDetail:
        return self.repository.details(id)

    def delete(self, business_user: str):
        return self.repository.delete(business_user)
