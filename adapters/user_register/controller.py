from typing import Any, Dict
from use_cases.user_register import Request, InputBoundary

class UserRegisterController:
    def __init__(self, input_boundary: InputBoundary):
        self.input_boundary = input_boundary

    def register_user(self, request: Dict[str, Any]):
        request: Request = Request(request['name'], request['password'])
        return self.input_boundary.register_user(request)
