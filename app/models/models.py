from pydantic import BaseModel


class User(BaseModel):
    name: str
    id: int


class UserAdult(BaseModel):
    name: str
    age: int

    def validate_age(self):
        return self.age >= 18
