from dataclasses import dataclass
from use_cases.user_register import Response, OutputBoundary

@dataclass
class ViewModel:
    name: str
    creation_time: str
    error: str

class UserRegisterPresenter(OutputBoundary):
    def success(self, response: Response) -> ViewModel:
        return ViewModel(response.name, response.creation_time, error='')

    def error(self, error: str) -> ViewModel:
        return ViewModel('', '', error=error)
