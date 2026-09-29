from models.comportement import Comportement
from models.actions.action_attaque_double import ActionAttaqueDouble
from models.actions.action_attaque import ActionAttaque
from models.actions.action_defense import ActionDefense

class ComportementBoss(Comportement):
    
    def agir(self, ennemi) -> str:
        if ennemi.hp > ennemi.hp_max * 0.6:
            return ActionDefense()
        elif ennemi.hp_max * 0.6 >= ennemi.hp > ennemi.hp_max * 0.3:
            return ActionAttaque()
        else:
            return ActionAttaqueDouble()
    
    def __str__(self) -> str:
        return "boss"