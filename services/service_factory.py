from dependency_injector import containers, providers
from typing import Callable

from .repositories.customer_repository import *
from .repositories.b_o_repositories import *
from .repositories.user_repository import *
from .repositories.staff_repository import *

from .service.customer_services import *
from .service.business_owner import *
from .service.UserServices import *
from .service.staff import *


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    customer_repository: Callable[[], CustomerRepository] = providers.Factory(
        DjangoORMForCustomerRepository,
    )

    business_owner_repository: Callable[[], BusinessRepository] = providers.Factory(
        DjangoORMForBusinessOwner,
    )

    user_repository: Callable[[], UserRepository] = providers.Factory(
        DjangoORMForUserRepository,
    )

    staff_repository: Callable[[], Staff_Repository] = providers.Factory(
        DjangoORMForStaffRepository,
    )

    customer_management_service: Callable[[], CustomerServices] = providers.Factory(
        DefaultDjangoServicesForCustomer,
        repository=customer_repository
    )

    business_owner_service: Callable[[], CustomerServices] = providers.Factory(
        DefaultOwnerServices,
        repository=business_owner_repository
    )

    user_services: Callable[[], UserManagementServices] = providers.Factory(
        DefaultUserManagementService,
        repository=user_repository
    )

    staff_services: Callable[[], Staff_Services] = providers.Factory(
        DefaultServicesForStaffs,
        repository=staff_repository
    )


service_container = Container()