import unittest

from flask import Response

from adapters.user_register.presenter import ViewModel
from entities.user import UserFactory
from use_cases.user_register import Request, UserModel, UserRegisterInteractor, UserModelGateway, OutputBoundary

user_request = Request("testuser123", "123456")

class UserModelGatewayTestImpl(UserModelGateway):
    def exists_by_name(self, _: str) -> bool:
        return False

    def save(self, _: UserModel) -> None:
        pass
    
class UserRegisterTestPresenter(OutputBoundary):
    def success(self, response: Response) -> ViewModel:
        return ViewModel(response.name, response.creation_time, error='')

    def error(self, error: str) -> ViewModel:
        return ViewModel('', '', error=error)

class TestUserRegisterInteractor(unittest.TestCase):
    def test_create_user(self):
        user_model_gateway = UserModelGatewayTestImpl()
        output_boundary = UserRegisterTestPresenter()
        user_factory = UserFactory

        interactor = UserRegisterInteractor(user_model_gateway, output_boundary, user_factory)
        response = interactor.register_user(user_request)
        
        self.assertEqual(response.name, "testuser123")

if __name__ == '__main__':
    unittest.main()
