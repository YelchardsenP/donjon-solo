from models.comportements.comportement import Comportement


class ComportementDefensif(Comportement):

    def agir(self, ennemi) -> str:
        return "defend"
    
    def __str__(self) -> str:
        return "defensif"