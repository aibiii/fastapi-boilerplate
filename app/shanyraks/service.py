from pydantic import BaseSettings

from app.config import database

from .adapters.jwt_service import JwtService
from .repository.repository import ShanyrakRepository

class Service:
    def __init__(
        self,
        repository: ShanyrakRepository,
        jwt_svc: JwtService,
    ):
        self.repository = repository
        self.jwt_svc = jwt_svc


def get_service():
    repository = ShanyrakRepository(database)
    jwt_svc = JwtService(config.JWT_ALG, config.JWT_SECRET, config.JWT_EXP)

    svc = Service(repository, jwt_svc)
    return svc