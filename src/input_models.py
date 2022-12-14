#!/usr/bin/env python

"""Defines input data structures used in the API endpoints."""

__author__ = 'Dr. Rudolf Jagdhuber'
__status__ = 'Development'

import pydantic


class TokenInput(pydantic.BaseModel):
    token: str


class ChangePasswordInput(pydantic.BaseModel):
    user_id: str
    old_password: str
    new_password: str
    token: str


class ChangeNameInput(pydantic.BaseModel):
    user_id: str
    password: str
    new_name: str
    token: str


class DeleteUserInput(pydantic.BaseModel):
    user_id: str
    password: str
    token: str


class LoginInput(pydantic.BaseModel):
    name: str
    password: str
    token: str


class NewGameInput(pydantic.BaseModel):
    user_id: str
    length: int
    tries: int
    word_id: int = -1  # -1 means to draw a random id that was not played yet.
    token: str


class GuessInput(pydantic.BaseModel):
    game_id: str
    guess: str
    token: str
