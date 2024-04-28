from pydantic import BaseModel


class administrator(BaseModel):
    name : str
    email : str
    phone :int
    address :str
    role :str
    accesslevel : str


    class Config:
        orm_mode = True