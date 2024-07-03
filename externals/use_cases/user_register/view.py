from typing import Any, Dict

from adapters.user_register.controller import UserRegisterController
from adapters.user_register.presenter import UserRegisterPresenter, ViewModel
from entities.user import UserFactory
from externals.db import db
from externals.use_cases.user_register.data import UserModelGatewayImpl
from use_cases.user_register import UserRegisterInteractor

output_boundary = UserRegisterPresenter()
user_factory = UserFactory()
user_model_gateway = UserModelGatewayImpl(db_session=db.session)
interactor = UserRegisterInteractor(user_model_gateway, output_boundary, user_factory)
controller = UserRegisterController(interactor)
    
def user_register_view(data: Dict[str, Any]) -> ViewModel:
    return controller.register_user(data)
