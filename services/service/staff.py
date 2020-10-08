from services.models import Staff
from abc import ABCMeta, abstractmethod
from typing import List
from services.dto.staff_dto import UpdateStaff, ListStaffs, StaffDetails, CreateStaff
from services.repositories.staff_repository import Staff_Repository


class Staff_Services(metaclass=ABCMeta):

    @abstractmethod
    def create(self, model: CreateStaff):
        '''creates a staff'''
        raise NotImplementedError


    @abstractmethod
    def update(self, id: int, model: UpdateStaff):
        """updates a staff record"""
        raise NotImplementedError

    @abstractmethod
    def details(self, id: int) -> StaffDetails:
        """shows a staff detail"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, id):
        """deletes a staff"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListStaffs]:
        """list all staffs"""
        raise NotImplementedError


class DefaultServicesForStaffs(Staff_Services):
    repository: Staff_Repository = None

    def __init__(self, repository: Staff_Repository):
        self.repository = repository

    def create(self, model: CreateStaff):
        return self.repository.create(model)

    def update(self, id: int, model: UpdateStaff):
        return self.repository.update(id, model)

    def list(self) -> List[ListStaffs]:
        return self.repository.list()

    def details(self, id: int) -> StaffDetails:
        return self.repository.details(id)

    def delete(self, id):
        return self.repository.delete(id)