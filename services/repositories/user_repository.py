from services.dto.Userdto import UserCreateDto, UserListDto, UserDetailDto
from django.contrib.auth.models import User
from abc import ABCMeta, abstractmethod
from typing import List


class UserRepository(metaclass=ABCMeta):
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


class DjangoORMForUserRepository(UserRepository):
    def create(self, model: UserCreateDto):
        user = User()
        user.username = model.username
        user.password = model.password
        user.email = model.email

        user = User.objects.create_user(user.username, user.email, user.password)

        user.first_name = model.first_name
        user.last_name = model.last_name
        user.save()

    def listUsers(self) -> List[UserListDto]:
        users = list(User.objects.values(
            'id',
            'first_name',
            'last_name',
            'username',
            'email'
        ))
        result: List[UserListDto] = []
        for user in users:
            model = UserListDto()
            model.id = user['id']
            model.first_name = user['first_name']
            model.last_name = user['last_name']
            model.username = user['username']
            model.email = user['email']
            result.append(model)
        return result

    def userDetails(self, id: int) -> UserDetailDto:
        try:
            user = User.objects.get(id=id)
            model = UserDetailDto()
            user.first_name = model.first_name
            user.last_name = model.last_name
            user.username = model.username
            user.email = model.email
            return model
        except User.DoesNotExist as e:
            print('user does not exist')
            raise e

    def deleteUser(self, id: int):
        try:
            user = User.objects.get(id=id)
            user.delete()
        except User.DoesNotExist as e:
            print('user does not exist')
            raise e
