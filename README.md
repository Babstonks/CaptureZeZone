# CaptureZeZone
A CTF inspired by The Towers (Minecraft)

## Contexte & cahier des charges
Développé dans le cadre d'une formation, pour un formateur pour monter en compétence en Python.

## Règles du jeu
### Maquette :
-  ![Maquette](https://github.com/Babstonks/CaptureZeZone/assets/76537635/11055745-8aed-4056-9d10-bae3c3d1be79)
#### violet 
générateur de blocks 
#### rouge 
zone de score
#### vert 
zone de heal
#### bleu
points de spawn

### Objectifs :
-  Pour gagner il faut marquer le plus de points dans le temps imparti.
-  Pour marquer des points les joueurs doivent se rendrent dans la zone adverse.
-  Les joueurs doivent construire des ponts vers la base adverse avec des blocs qu'ils récupèrent dans leur base.
-  Les joueurs peuvent se tirer dessus et casser les blocs adverses pour les empecher de marquer des points.

## Use cases
- pour l'administrateur
Expliquer ce que peut/doit faire un administrateur qui souhaite lancer/administrer une arène de jeu avec des apprenants 

- pour le joueur
Renvoyer vers README API

## User story :
- Le joueur apparaît du côté de son équipe aux niveaux d'un des deux point de spawn.
- Le joueur doit pouvoir se déplacer à travers la carte pour atteindre la zone à capturer.
- Le joueur doit contourner les obstacles présents sur la carte et ne peut se déplacer dans le vide.
- Le joueur doit pouvoir récupérer des blocks dans les zones prévues dans la base.
- Le joueur doit pouvoir tirer sur ses adversaires pour les empécher d'atteindre leur zone.
- Le joueur doit pouvoir poser ses blocks pour atteindre la base adverse.
- Le joueur doit pouvoir casser les blocks des joueurs adverses. 

## Pré-requis 
- pour l'administrateur
Matériel et logiciel requis pour executer votre projet
- pour les apprenants 
Rediriger vers README API

## Tests
- définition du plan de test ce qu'on attend quand on fait quoi

#### test_placeBlock
- Ce test garantit que la méthode placeBlock du joueur modifie correctement l'attribut de couleur de l'agent du joueur. Il vérifie que, après l'appel à placeBlock, le deuxième élément de l'attribut de couleur de l'agent est égal à 3.

#### test_moveTowards
- L'objectif de ce test est de valider la méthode moveTowards du joueur. Il simule un déplacement vers les coordonnées (1, 2) et vérifie si les coordonnées de l'agent du joueur sont correctement mises à jour à (1, 2) après le déplacement.

#### test_getCoordinates
- Ce test se concentre sur la méthode getCoordinates du joueur. Il définit des coordonnées spécifiques x et y pour l'agent du joueur, appelle getCoordinates et vérifie que le résultat retourné correspond aux coordonnées attendues (3, 4).

## Auteur(s)
DEMEILLIERS léo - LEVIEUX Tristan - CAILLY Bastien

## License
MIT license
