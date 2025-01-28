# 2048

**Auteur**: Ahmet KARABULUT  
**Version**: 1.0  
**Date**: 28.01.2025

---

## Description

Ce projet est une implémentation du jeu classique **2048** en Python, avec une interface graphique simple construite à l'aide de **Tkinter**. Le but du jeu est de combiner des cases ayant les mêmes valeurs pour atteindre la valeur 2048 (ou plus) sur une grille 4x4.

---

## Fonctionnalités

- **Mouvement des cases** : Utilisation des flèches directionnelles (← ↑ → ↓) pour déplacer les cases.
- **Fusion des cases** : Les cases avec les mêmes valeurs se combinent pour former une nouvelle case avec une valeur doublée.
- **Génération aléatoire** : Une nouvelle case (valeur 2 ou 4) est ajoutée après chaque mouvement.
- **Interface intuitive** : Les cases changent de couleur en fonction de leur valeur.

---

## Prérequis

- Python 3.8 ou supérieur
- Bibliothèques standard de Python (Tkinter)

---

## Installation

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/votre-utilisateur/2048.git
   cd 2048
   ```

2. **Exécuter le script** :
   ```bash
   python 2048.py
   ```

---

## Règles du jeu

1. Utilisez les flèches directionnelles pour déplacer toutes les cases dans une direction.
2. Lorsque deux cases ayant la même valeur se rencontrent, elles fusionnent en une seule case avec une valeur doublée.
3. Une nouvelle case (valeur 2 ou 4) est ajoutée à une position aléatoire après chaque mouvement.
4. Le jeu se termine lorsque plus aucun mouvement n'est possible.
5. Le but est d’atteindre une case de valeur **2048** (ou plus) pour gagner.

---

## Structure du projet

- **2048.py** : Fichier principal contenant le code du jeu.
- **README.md** : Documentation du projet (ce fichier).

---

## Aperçu visuel

L'interface se compose d'une grille 4x4 avec des cases colorées qui représentent les différentes valeurs :

|    |    |    |    |
|----|----|----|----|
| 2  | 4  | 8  | 16 |
| 32 | 64 | 128| 256|
| 512|1024|2048|    |
|    |    |    |    |

---

## Contrôles

- **Flèche gauche (←)** : Déplace les cases vers la gauche.
- **Flèche droite (→)** : Déplace les cases vers la droite.
- **Flèche haut (↑)** : Déplace les cases vers le haut.
- **Flèche bas (↓)** : Déplace les cases vers le bas.

---

## Personnalisation

Vous pouvez personnaliser les couleurs des cases et la disposition initiale en modifiant les variables suivantes dans le fichier **2048.py** :

- **`game`** : Liste 2D représentant la grille initiale.
- **`colors`** : Dictionnaire associant chaque valeur à une couleur.

---

## Exemple de grille initiale

```python
game = [
    [0, 2, 4, 8],
    [16, 32, 0, 128],
    [256, 0, 1024, 2048],
    [0, 0, 0, 0]
]
```

---

## Améliorations futures

- Ajouter un système de score visible.
- Inclure un bouton "Nouvelle partie".
- Enregistrer les meilleurs scores.
- Ajouter des animations pour les mouvements et les fusions.

---

## Auteur

Ahmet KARABULUT  
[Email](mailto:ahmet.karabulu@example.com)  

---

## Licence

Ce projet est sous licence MIT. Vous êtes libre de l'utiliser, de le modifier et de le redistribuer.

