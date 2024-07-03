
from dataclasses import dataclass
from typing import Any, Dict, Protocol
from datetime import datetime, timezone
from entities.user import UserFactory

@dataclass
class Request:
    name: str
    password: str

@dataclass
class Response:
    name: str
    creation_time: str

class InputBoundary(Protocol):
    def register_user(self, request: Request) -> Dict[str, Any]:
        pass

class OutputBoundary(Protocol):
    def success(self, response: Response) -> Dict[str, Any]:
        pass

    def error(self, error: str) -> Dict[str, Any]:
        pass

@dataclass  
class UserModel:
    name: str
    password: str
    creation_time: str

class UserModelGateway(Protocol):
    def exists_by_name(self, name: str) -> bool:
        pass

    def save(self, user_model: UserModel) -> None:
        pass

class UserRegisterInteractor(InputBoundary):
    def __init__(self, user_model_gateway: UserModelGateway, output_boundary: OutputBoundary, user_factory: UserFactory):
        self.user_model_gateway = user_model_gateway
        self.output_boundary = output_boundary
        self.user_factory = user_factory

    def register_user(self, request: Request):
        if self.user_model_gateway.exists_by_name(request.name):
            return self.output_boundary.error("User already exists.")
        
        user = self.user_factory.create(request.name, request.password)
        if not user.password_is_valid():
            return self.output_boundary.error("User password must have more than 5 characters.")
        
        now = datetime.now(timezone.utc)
        user_model = UserModel(user.name, user.password, now)
        self.user_model_gateway.save(user_model)
        
        response = Response(user_model.name, now.strftime('%H:%M:%S'))
        return self.output_boundary.success(response)
