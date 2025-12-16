from typing import List, Union

from pydantic import BaseModel


class Error400(BaseModel):
    detail: str = "Incorrect email or password"


class Error401(BaseModel):
    detail: str = "Not authenticated"


class Error404(BaseModel):
    detail: str = "Item not found"


class DetailItem(BaseModel):
    loc: List[Union[str, int]]
    msg: str
    type: str


class Error422(BaseModel):
    detail: List[DetailItem]
