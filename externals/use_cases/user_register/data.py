from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from use_cases.user_register import UserModel, UserModelGateway


class Base(DeclarativeBase):
    pass


class UserModelDataMapper(Base):
    __tablename__ = 'user'

    name: Mapped[str] = mapped_column(primary_key=True)
    password: Mapped[str]
    creation_time: Mapped[datetime]
    
    def __init__(self, name: str, password: str, creation_time: str):
        self.name = name
        self.password = password
        self.creation_time = creation_time

class UserModelGatewayImpl(UserModelGateway):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def exists_by_name(self, name: str) -> bool:
        return self.db_session.query(UserModelDataMapper).filter_by(name=name).first() is not None

    def save(self, user: UserModel) -> None:
        user_data_mapper = UserModelDataMapper(user.name, user.password, user.creation_time)
        self.db_session.add(user_data_mapper)
        self.db_session.commit()
