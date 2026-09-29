# Projet 2 — Le Donjon des Algorithmes

## Présentation du jeu

Vous êtes un héros qui explore un donjon et affronte des vagues d'ennemis.
Chaque ennemi a une **tactique de combat** différente — certains attaquent
toujours, d'autres se protègent quand ils sont affaiblis, d'autres encore
sont imprévisibles.

---

## Mécanisme du jeu

### Les acteurs

| Acteur | HP | Attaque |
|---|---|---|
| Héros | 100 | 20 |
| Goblin | 50 | 10 |
| Dragon | 100 | 20 |
| Voleur | 30 | 15 |

### Déroulement d'un tour

1. L'état du combat s'affiche — HP du héros et liste des ennemis
2. Le héros choisit son action : **attaquer** un ennemi ou **se défendre**
3. Chaque ennemi agit selon son **comportement actuel** (expliqué plus bas)
4. Les dégâts sont calculés et appliqués
5. Le tour suivant commence

### Calcul des dégâts

| Héros | Ennemi | Résultat |
|---|---|---|
| Attaque | Attaque | Échange de coups — chacun inflige ses dégâts complets |
| Attaque | Défend | Héros inflige la moitié des dégâts — ennemi n'attaque pas |
| Défend | Attaque | Ennemi inflige la moitié des dégâts — héros n'attaque pas |
| Défend | Défend | Rien ne se passe |

### Conditions de fin

- **Victoire** : tous les ennemis sont à 0 HP
- **Défaite** : le héros est à 0 HP

---

## Les comportements d'ennemis

C'est le cœur du projet. Chaque ennemi a un comportement qui détermine
s'il attaque ou se défend à chaque tour :

| Comportement | Description |
|---|---|
| **Agressif** | Attaque toujours, peu importe son état |
| **Défensif** | Se défend si ses HP sont sous 50%, attaque sinon |
| **Aléatoire** | Choisit aléatoirement à chaque tour |
| **Furtif** | Alterne — défend un tour, attaque le suivant |

Les ennemis sont créés avec un comportement initial, mais peuvent **changer de comportement** en cours selon la règle suivante:

- Tout ennemi dont les HP tombent sous **30%** de ses HP maximum bascule
  automatiquement en mode **Défensif**, peu importe son comportement initial.

Par exemple, un Goblin Agressif qui commence à 50 HP deviendra Défensif
dès qu'il tombe sous 15 HP.

---

## Travail à faire avant le cours

1. Forkez ce dépôt sur votre compte GitHub
2. Lancez `python main.py` et jouez quelques tours pour comprendre le jeu
3. Lisez attentivement le code et posez-vous les questions suivantes :
   - Que fait la méthode `agir()` de la classe `Ennemi` ?
   - Que faudrait-il modifier pour ajouter un comportement "Berserk" qui double ses dégâts quand ses HP sont sous 25% ?
   - Que faudrait-il modifier pour qu'un Goblin puisse changer de comportement en cours de partie ?
   - Y a-t-il de la duplication dans le code ?

---

## Exemple de partie

```
===========================================
        LE DONJON DES ALGORITHMES
===========================================

Tour 1 — Héros : 100 HP

Ennemis :
  [1] Goblin  (HP: 50)  — Agressif
  [2] Dragon  (HP: 100) — Défensif
  [3] Voleur  (HP: 30)  — Furtif

Votre action ? (a)ttaquer / (d)éfendre : a
Quel ennemi ? (1/2/3) : 1

--- Résultats ---
Vous attaquez le Goblin pour 20 dégâts !
  → Goblin : 50 HP → 30 HP
  → Le Goblin vous attaque pour 10 dégâts !
  → Le Dragon se défend. Pas d'échange.
  → Le Voleur disparaît dans l'ombre...

Héros : 90 HP
===========================================
Tour 2
```
