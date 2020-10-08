from abc import ABCMeta, abstractmethod
from services.dto.business_dto import BusinessUpdateDto, ListBusinessOwner, BusinessOwnerDetail
from services.models import BusinessOwner
from typing import List


class BusinessRepository(metaclass=ABCMeta):

    @abstractmethod
    def update(self, business_user: str, model: BusinessUpdateDto):
        """updates a customer object"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListBusinessOwner]:
        """list all available business owners"""
        raise NotImplementedError

    @abstractmethod
    def details(self, business_user: str) -> BusinessOwnerDetail:
        """shows the details of a business owner"""
        raise NotImplementedError


class DjangoORMForBusinessOwner(BusinessRepository):

    def update(self, id: int, model: BusinessUpdateDto):
        try:
            businessOwner = BusinessOwner.objects.get(id=id)
            businessOwner.phone_no = model.phone_no
            businessOwner.company_name = model.company_name
            businessOwner.company_address = model.company_address
            businessOwner.service_title = model.service_title
            businessOwner.service_description = model.service_description
            businessOwner.CAC_code = model.CAC_code
            businessOwner.guarantors_name = model.guarantors_name
            businessOwner.guarantor_phone_no = model.guarantors_phone_no
            businessOwner.guarantors_address = model.guarantors_address
            businessOwner.save()
        except BusinessOwner.DoesNotExist as error:
            print('No business owner with that name')
            raise error

    def list(self) -> List[ListBusinessOwner]:
        owners = list(BusinessOwner.objects.values(
            'id',
            'user__username',
            'phone_no',
            'company_name',
            'company_address',
            'service_title',
        ))
        values: ListBusinessOwner = []
        for owner in owners:
            value = ListBusinessOwner()
            value.id = owner['id']
            value.user = owner['user__username']
            value.phone_no = owner['phone_no']
            value.company_name = owner['company_name']
            value.company_address = owner['company_address']
            value.service_title = owner['service_title']
            values.append(value)
        return values

    def details(self, id: int) -> BusinessOwnerDetail:
        try:
            owner = BusinessOwner.objects.get(id=id)
            detail = BusinessOwnerDetail()
            detail.user = owner.user
            detail.phone_no = owner.phone_no
            detail.company_name = owner.company_name
            detail.company_address = owner.company_address
            detail.service_title = owner.service_title
            return detail
        except BusinessOwner.DoesNotExist as error:
            print('No record for the given id')
            raise error

