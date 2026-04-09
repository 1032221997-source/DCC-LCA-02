from pydantic import BaseModel

class URLRequest(BaseModel):
    url:str


class ContentRequest(BaseModel):
    title:str
    content:str
