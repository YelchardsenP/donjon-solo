import time
from models.ennemi import Ennemi
from models.comportements.co_agressif import ComportementAgressif
from models.comportements.co_defensif import ComportementDefensif
from models.comportements.co_aleatoire import ComportementAleatoire
from models.comportements.co_furtif import ComportementFurtif
from models.comportements.co_berserker import ComportementBerserker


class Jeu:
    def __init__(self):
        self.heros_hp = 1000
        self.heros_hp_max = 1000
        self.heros_attaque = 25

        self.ennemis = [
            Ennemi("Goblin",  hp=50,  attaque=8,  comportement=ComportementAgressif()),
            Ennemi("Dragon",  hp=100, attaque=12, comportement=ComportementDefensif()),
            Ennemi("Spectre", hp=40,  attaque=10, comportement=ComportementAleatoire()),
            Ennemi("Voleur",  hp=30,  attaque=10, comportement=ComportementFurtif()),
            Ennemi("Son Goku", hp=200, attaque=10, comportement=ComportementBerserker())
        ]

    def ennemis_vivants(self):
        return [e for e in self.ennemis if e.est_vivant()]

    def demarrer(self):
        print("\n===========================================")
        print("        LE DONJON DES ALGORITHMES")
        print("===========================================\n")

        tour = 1

        while self.heros_hp > 0 and self.ennemis_vivants():
            # Afficher l'état
            print(f"Tour {tour} — Héros (HP: {self.heros_hp}/{self.heros_hp_max})")
            print("\nEnnemis :")
            vivants = self.ennemis_vivants()
            for i, ennemi in enumerate(vivants, 1):
                print(f"  [{i}] {ennemi.nom} (HP: {ennemi.hp}/{ennemi.hp_max}) — {ennemi.get_comportement()}")
            print()

            # Demander l'action du héros
            while True:
                action = input("Votre action ? (a)ttaquer / (d)éfendre : ").strip().lower()
                if action in ["a", "d", "x", "m"]:
                    break
                print("Choix invalide.")
            action_heros = "attaque" if action == "a" else "genkidama" if action == "x" else "murasaki" if action == "m" else "defend"

            
            
            # Demander la cible si attaque
            cible = None
            if action_heros == "attaque":
                if len(vivants) == 1:
                    cible = vivants[0]
                else:
                    while True:
                        try:
                            choix = int(input(f"Quel ennemi ? (1-{len(vivants)}) : "))
                            if 1 <= choix <= len(vivants):
                                cible = vivants[choix - 1]
                                break
                        except ValueError:
                            pass
                        print("Choix invalide.")
                    
            # Chaque ennemi décide de son action
            actions_ennemis = {e: e.agir() for e in vivants}

            

            print("--- Résultats ---")

            #Attaque secrète ultime 1
            #emojis hollow purple : 🔴🌀🌑✨🌌
            if action_heros == "genkidama":
                print("\n🌌 Vous levez les mains vers le ciel...")
                time.sleep(1)

                print("✨ L'énergie commence à se rassembler...")
                time.sleep(1)

                for i in range(5):
                    print(" " * (10 - i) + "✨")
                    time.sleep(0.3)

                print("""
                            🌌🌌
                        🌌🌌🌌🌌🌌
                    🌌🌌🌌🌌🌌🌌🌌🌌
                   🌌🌌🌌🌌🌌🌌🌌🌌🌌
                    🌌🌌🌌🌌🌌🌌🌌🌌
                        🌌🌌🌌🌌🌌
                            🌌🌌

                     ✨🌀 GENKIDAMA !!! 🌀✨
                """)

                time.sleep(1)

                print("💥💥💥 KABOOMMMM 💥💥💥")
                time.sleep(1)

                for i in range(3):
                    print("💥" * (i + 1) * 5)
                    time.sleep(0.3)

                # Anéantit la moitié des hp tous les ennemis
                for ennemi in vivants:
                    ennemi.recevoir_degats(ennemi.hp_max * 0.5)

                print("\n☠️ Tous les ennemis ont perdu la moitié de leur santé !")
                time.sleep(1)
            
            #Attaque secrète ultime 2
            #emojis hollow purple : 🔴🌀🌑✨🌌
            if action_heros == "murasaki":
                print("\n🔴🔴Le rouge..🔴🔴")
                time.sleep(1)

                print("✨ 🌀🌀Le bleu..🌀🌀")
                time.sleep(1)

                print("🔴       🌀")
                time.sleep(0.1)

                print("🔴      🌀")
                time.sleep(0.1)

                print("🔴     🌀")
                time.sleep(0.1)

                print("🔴   🌀")
                time.sleep(0.1)

                print("🔴   🌀")
                time.sleep(0.1)

                print("🔴  🌀")
                time.sleep(0.1)

                print("🔴 🌀")
                time.sleep(0.1)

                print("🔴🌀")
                time.sleep(0.1)

                print("🔴🌑🌑🌑🌀")
                time.sleep(0.5)

                print("🌑🌑🌑")
                time.sleep(1)

            

                # Anéantit la moitié des hp tous les ennemis
                for ennemi in vivants:
                    ennemi.recevoir_degats(ennemi.hp)

                print("\n☠️ Tous les ennemis ont été anéantis !")
                time.sleep(1)
            

            # Résoudre l'attaque du héros
            if action_heros == "attaque" and cible:
                if actions_ennemis.get(cible) == "defend":
                    degats = self.heros_attaque // 2
                    print(f"Vous attaquez {cible.nom} — il se défend ! Seulement {degats} dégâts infligés.")
                else:
                    degats = self.heros_attaque
                    print(f"Vous attaquez {cible.nom} pour {degats} dégâts !")
                cible.recevoir_degats(degats)
            
            # Résoudre les actions des ennemis
            for ennemi, action_ennemi in actions_ennemis.items():
                if not ennemi.est_vivant():
                    continue
                action_ennemi = ennemi.agir()       # ← un objet Action
                self.heros_hp, msg = action_ennemi.appliquer(ennemi, self.heros_hp, action_heros)
                print(msg)
            tour += 1

        if self.heros_hp > 0:
            print("\n===========================================")
            print("  🏆 VICTOIRE ! Tous les ennemis sont vaincus !")
            print("===========================================\n")
        else:
            print("\n===========================================")
            print("  💀 DÉFAITE ! Le héros est tombé...")
            print("===========================================\n")
