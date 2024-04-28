from pydantic import BaseModel


class labtest(BaseModel):
    name : str
    dob : int
    testordered = Column(String)
    status = Column(String)
    testresult = Column(String)
    title: str
    rating: int

    class Config:
        orm_mode = True