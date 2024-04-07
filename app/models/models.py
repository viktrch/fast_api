from pydantic import BaseModel, EmailStr, PositiveInt


class User(BaseModel):
    name: str
    id: int


class UserAdult(BaseModel):
    name: str
    age: int

    def validate_age(self):
        return self.age >= 18


class Feedback(BaseModel):
    name: str
    message: str

    def get_success_message(self):
        return {'message': f'Feedback received. Thank you, {self.name}!'}


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: PositiveInt | None = None
    is_subscribed: bool | None = None
