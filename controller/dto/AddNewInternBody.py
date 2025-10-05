from pydantic import BaseModel
class AddNewInternBody(BaseModel):
    name : str
    mailId : str
    hobbies : str