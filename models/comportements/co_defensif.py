from models.comportements.comportement import Comportement
from models.actions.action_defense import ActionDefense


class ComportementDefensif(Comportement):

    def agir(self, ennemi) -> str:
        return ActionDefense()
    
    def __str__(self) -> str:
        return "defensif"