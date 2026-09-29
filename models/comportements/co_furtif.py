from models.comportements.comportement import Comportement
from models.actions.action_attaque import ActionAttaque
from models.actions.action_defense import ActionDefense


class ComportementFurtif(Comportement):

    def __init__(self) -> None:
        self._tour = 0   

    def agir(self, ennemi) -> str:
        self._tour += 1
        if self._tour % 2 == 0:
            return ActionAttaque()
        return ActionDefense()

    def __str__(self) -> str:
        return "furtif"