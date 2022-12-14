#!/usr/bin/env python

"""Defines response data structures used in the API endpoints."""

__author__ = 'Dr. Rudolf Jagdhuber'
__status__ = 'Development'

import pydantic


class SimpleResponse(pydantic.BaseModel):
    message: str


class GenericUserResponse(pydantic.BaseModel):
    id: str
    name: str
    password: str


class LoginResponse(pydantic.BaseModel):
    id: str


class LetterCorrectnessResponse(pydantic.BaseModel):
    letter: str
    correct_position: bool
    different_position: bool


class WordCorrectnessResponse(pydantic.BaseModel):
    __root__: list[LetterCorrectnessResponse]


class GuessListResponse(pydantic.BaseModel):
    __root__: list[WordCorrectnessResponse]


class GameResponse(pydantic.BaseModel):
    id: str
    player: str
    word_id: int
    word: str | None
    length: int
    tries: int
    guesses: GuessListResponse | None
    created: str
    solved: int


class GameListResponse(pydantic.BaseModel):
    __root__: list[GameResponse]
