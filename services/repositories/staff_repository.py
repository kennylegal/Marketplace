from services.models import Staff
from abc import ABCMeta, abstractmethod
from typing import List
from services.dto.staff_dto import UpdateStaff, ListStaffs, StaffDetails, CreateStaff


class Staff_Repository(metaclass=ABCMeta):

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
    def list(self) -> List[ListStaffs]:
        """list all staffs"""
        raise NotImplementedError


class DjangoORMForStaffRepository(Staff_Repository):

    def create(self, model: CreateStaff):
        staff = Staff()
        staff.user = model.user
        staff.staff_code = model.staff_code
        staff.DOB = model.DOB
        staff.address = model.address
        staff.job_title = model.job_title
        staff.save()

    def update(self, id: int, model: UpdateStaff):
        try:
            staff = Staff.objects.get(id=id)
            staff.user = model.user
            staff.DOB = model.DOB
            staff.address = model.address
            staff.job_title = model.job_title
            staff.save()
        except Staff.DoesNotExist as error:
            print('User does not exist')
            raise error

    def list(self) -> List[ListStaffs]:
        staff = list(Staff.objects.values(
            'id',
            'user__username',
            'job_title',
            'staff_code'
        ))
        values: ListStaffs = []
        for staffs in staff:
            value = ListStaffs()
            value.id = staffs['id']
            value.user = staffs['user__username']
            value.job_title = staffs['job_title']
            value.staff_code = staffs['staff_code']
            values.append(value)
            return values

    def details(self, id: int) -> StaffDetails:
        try:
            staff = Staff.objects.get(id=id)
            detail = StaffDetails()
            detail.user = staff.user
            detail.staff_code = staff.staff_code
            detail.address = staff.address
            detail.job_title = staff.job_title
            return detail
        except Staff.DoesNotExist as error:
            print('staff does not exist')
            raise error
