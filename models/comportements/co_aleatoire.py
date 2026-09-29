import random
from models.comportements.comportement import Comportement


class ComportementAleatoire(Comportement):

    def agir(self, ennemi) -> str:
        return random.choice(["attaque", "defend"])

    def __str__(self) -> str:
        return "aléatoire"