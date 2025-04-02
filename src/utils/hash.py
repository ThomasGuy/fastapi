from dataclasses import dataclass

import bcrypt
from passlib.context import CryptContext


@dataclass
class SolveBugBcryptWarning:
    __version__: str = getattr(bcrypt, '__version__')  # noqa: B009


setattr(bcrypt, '__about__', SolveBugBcryptWarning())  # noqa: B010

pwd_ctx = CryptContext(schemes=['bcrypt'], deprecated='auto')


class Hash:
    @staticmethod
    def verify(hashed_password, plain_password):
        return pwd_ctx.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password):
        return pwd_ctx.hash(password)
