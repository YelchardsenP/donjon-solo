# models/comportement.py
from abc import ABC, abstractmethod


class Comportement(ABC):

    @abstractmethod
    def agir(self, ennemi) -> str:
        
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass