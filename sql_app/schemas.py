from pydantic import BaseModel

class TeaBase(BaseModel):
    name: str


class TeaCreate(TeaBase):
    type: str


class Tea(TeaBase):
    id: int

    class Config:
        orm_mode = True