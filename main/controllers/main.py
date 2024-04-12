# from fastapi.exceptions import ValidationError
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from enum import Enum
from fastapi.encoders import jsonable_encoder

app = FastAPI(
    title="Stankin_Diary",
)


# @app.exception_handler(ValidationError)
# async def validation_exception_handler(request: Request, exc: ValidationError):
#     return JSONResponse(
#         status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
#         content=jsonable_encoder({"detail": exc.errors()}),
#     )


@app.get("/user/{id}")
async def root(id: int):
    return {"message": f"Я сосу {id} хуёв"}


@app.get("/sign_up")
async def signUp(name: str):
    return {"message": f"Hello {name}"}


class DegreeType(Enum):
    student = "student"
    monitor = "monitor"


class Degree(BaseModel):
    id: int
    type_degree: DegreeType


class User(BaseModel):
    id: int
    role: str
    name: str
    degree: Optional[List[Degree]] = []
