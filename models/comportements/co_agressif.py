from models.comportements.comportement import Comportement
from models.actions.action_attaque import ActionAttaque


class ComportementAgressif(Comportement):

    def agir(self, ennemi) -> str:
        return ActionAttaque()

    def __str__(self) -> str:
        return "agressif"