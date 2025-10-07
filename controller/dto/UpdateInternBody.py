from pydantic import BaseModel
class UpdateInternBody(BaseModel):
    name : str
    mailId : str
    hobbies : str