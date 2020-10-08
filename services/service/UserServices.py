from services.repositories.user_repository import UserRepository
from services.dto.Userdto import UserListDto, UserCreateDto, UserDetailDto
from abc import ABCMeta, abstractmethod
from typing import List


class UserManagementServices(metaclass=ABCMeta):
    @abstractmethod
    def create(self, model: UserCreateDto):
        """creates a new user"""
        raise NotImplementedError

    @abstractmethod
    def listUsers(self) -> List[UserListDto]:
        """list all users"""
        raise NotImplementedError

    @abstractmethod
    def userDetails(self, id: int) -> UserDetailDto:
        """shows the details of a specific user"""
        raise NotImplementedError

    @abstractmethod
    def deleteUser(self, id: int):
        """deletes a user"""
        raise NotImplementedError


class DefaultUserManagementService(UserManagementServices):
    repository: UserRepository = None

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create(self, model: UserCreateDto):
        return self.repository.create(model)

    def listUsers(self) -> List[UserListDto]:
        return self.repository.listUsers()

    def userDetails(self, id: int) -> UserDetailDto:
        return self.repository.userDetails(id)

    def deleteUser(self, id: int):
        return self.repository.deleteUser(id)
