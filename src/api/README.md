## Introduction
Ce projet consiste en l'implémentation d'un joueur pour participer à un jeu basé sur la plateforme j2l.pytactx. Le joueur est développé en utilisant la classe Player qui hérite de l'interface IPlayer.

Comment rejoindre l'arène :
Créer un joueur de la façon suivante :

playerId: L'identifiant du joueur.
arena: Le nom de l'arène.
username: Votre nom d'utilisateur.
password: Votre mot de passe.
server: L'adresse du serveur.
port: Le port à utiliser (par défaut : 1883).
verbosity: Le niveau de verbosité (par défaut : 2).

Exemple : 
new_player = enterzezone.Player("joueur1", "enterzezone", "demo", "demo","mqtt.jusdeliens.com")

## Fonctionnalités du Joueur
Le joueur implémente les fonctionnalités suivantes, conformément à l'interface IPlayer :

getTeam(): Retourne le numéro de l'équipe du joueur.

getCoordinates(): Retourne les coordonnées actuelles du joueur (x, y).

getDirection(): Retourne la direction actuelle du joueur.

placeBlock(): Place un bloc devant le joueur.

move(): Déplace le joueur d'une unité dans sa direction actuelle.

moveTowards(x, y): Déplace le joueur vers les coordonnées spécifiées (x, y).

shoot(): Démarre le tir avec une portée d'un bloc.

updateSelf(): Met à jour les informations du joueur.

rotate(dir): Demande une rotation du joueur sur la grille vers la direction spécifiée (0 pour l'est, 1 pour le nord, 2 pour l'ouest, 3 pour le sud).
