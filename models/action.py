from abc import ABC, abstractmethod

class Action(ABC):

    @abstractmethod
    def appliquer(self, enenemi, heros_hp: int, action_heros: str) -> tuple[int, str]:
        """Applique action retourne un message décrivant l'action."""
        pass