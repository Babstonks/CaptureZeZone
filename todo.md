# ⚔️ Plan d'attaque de la conception du jeu
## 2023-11-13 TD & TP
- [x] Comprendre les bonnes pratiques à utiliser pour votre jeu
- [x] Comprendre les interactions entre les end points d'un jeu robotique réseau
- [x] Définir un groupe de 3-4 personnes
- [x] Créer un projet github/gitlab et partager les droits à toute l'équipe et jusdeliens-pedago
- [x] Partir de l'API, définir tous les use cases des utilisateurs joueurs sur un readme
- [x] Faire une maquette à insérer dans votre readme (figma, paint, powerpoint ...)
- [x] Lire le champs des possibles de votre arbitre sur tutos.jusdeliens
- [x] Définir et répartir les tâches dans un kanban (trello ou issues sur github) 
- [ ] Rédiger le diagramme de séquence pour chaque use case et présenter à l'enseignant
## 2023-11-14 TD & TP
- [x] Finalisation github (resources images, maquette, readme) + invitation
- [ ] Définition des arbitres et création des arènes
- [ ] Choisir interface/méthodes de votre API en Python
- [ ] Réaliser les tests unitaires et fonctionnels de l'API
- [ ] Définir les responsabilités de chaque arbitre : initialisation resources, gestion score, gestion carte ...

# 🤼‍♀️ Les groupes
## TD2
- Flappy plane (flappy bird): Samy VASSE, Augustin BUKIN, Teiva TESSON, Théo LEBIEZ
    arena : flappyplane
    ❎https://github.com/Deeffault/pytactx-FlappyPlane
- TurboVroum (trackmania): Romain LESIEUR, Thomas PLANTAIS, Mylan MEGARD, Mathieu ORDONNAUD
    arena : turbovroum
    ❎https://github.com/ThomasHawk11/pytactxv2_race
- Huntastic (Poule renard vipère) : Eva POTTIER, Thanina GUERNINE, Hugo LE COUPANEC
    arena : huntastic
    ❎https://github.com/Thaninux/Huntastic
    
- Flash Siklik (Tron): Tristan BELLAN, Théo DUVAL, Baptiste CHERUEL, Hugo BOUCHAUD 
    arena : flashsiklik
    ❎https://github.com/Miokido/flash-siklik
    manque descriptions, resources (maquette, logo)
- A Mazing Tower (labyrinthe): Thomas FEDORAWIEZ, Pierre TOITOT, HARNOIS Léo, Antoine CLERICE
    arena : amazingtower
    ❎https://github.com/LighTend3r/A-Mazing-Tower
- Hunt ze zone (CTF) : Léo DEMEILLIERS, Bastien CAILLY, Tristan LEVIEUX
    arena : huntzezone
    ❎https://github.com/Babstonks/CaptureZeZone

## TD1
- Potato Blast: Romain LECOUVREUR, Victorien GONTIER-DURAND, Samuel LAUNAY
    arena : potatoblast
    ❎ Manque invitation github
- C.R.A-sion (super crate box): Hugo MARTIN, Clément SEVAUX
    arena : crasion
    ❎https://github.com/Frexom/C.R.A-sion/invitations
- ConflictTowers (Clash des titans carte): Gaëtan LANGLOIS, Thibaud LEBRASSEUR, Damien LEROY
    arena : conflicttower
    ❎https://github.com/DAMIENLRY/ConflictTower
- Pysurfer: Théo PEREIRA, Benoit PLISSIONNIER, Victor FOUQUET, Sacha DESQUESNES
    arena : pysurfer
    ❎https://gitlab.com/dev_per/pysurfer

- Rattlesli.de (slither.io): Célia DENNETIERE, Valentin GUILLOT, Jean-Victor, Léo MAFILLE
    arena : rattleslide
    ❎https://github.com/Eclelia/Rattlesli.de
- Survival Waves (zombies): Clément CAILLY, Arthur DESOMONTS, Alexandre ANGOT, Hélie TOLLEMER
    arena : survivalwaves
    ❎https://github.com/ccailly/SurvivalWaves
- Bubble Hell: Faustine GORLAS, Iona QUERNE, Eva-Marie HAMEL
    arena : bubblehell
    ❎https://github.com/Eva-Marie-Hamel/Bubble-Hell

# 📂 Arborescence projet Github
- votrejeu
    - doc
        - *.svg
    - src
        - api
            - j2l           -> *lib jusdeliens à récupérer sur tutos.jusdeliens.com* 
            - votrejeu.py   -> *interface API de votre jeu côté client*
            - readme.md     -> *explique au joueur les actions possibles de l'api*
        - server
            - res           -> *dossier des ressources de votre jeu*
            - main.py       -> *logique backend implémentant les règles du jeu*
    - tests
        - api
            - test_votrejeu.py
        - server
            - test_main.py
    - readme.md             -> *inclus diagramme de conception du dossier doc*

# 💻 Dev de votre API en TDD
1. Définir l'interface de l'API du jeu pour respecter les US de l'utilisateur joueur
    - 1 méthode update() pour actualiser votre classe joueur et synchroniser son état et requêtes avec le server
    - 1 constructeur prennant en paramètre au minimum : playerId, arena, le serveur et son port, username et password
    ⚠️ Méthodes et attributs en anglais, avec la même convention de nommage (en snake case ou camel case) 

2. Créer fichier .env en mettant les credentials de votre arène
    ⚠️ ** RAJOUTER DANS GIT IGNORE CE .env POUR NE PAS COMMIT LES MOTS DE PASSE"
    - install dotenv
    ```bash
    pip install python-dotenv
    ```
    - créer votre fichier à la racine du dossier projet
    ```
    # environment variables defined inside a .env file
    ARENA=votrejeu
    SERVER=mqtt.jusdeliens.com
    PORT=1883
    USERNAME=demo
    PASSWORD=demo
    ```
    - charger votre env dans chaque fichier où vous avez besoin des credentials de l'arène
    ```python
    import os
    from dotenv import load_dotenv
    load_dotenv()
    ARENA = os.getenv('ARENA')
    SERVER = os.getenv('SERVER')
    PORT = os.getenv('PORT')
    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')
    ``` 

3. Ecrire les tests de l'interface dans le fichier "test_*" correspondant à chaque fichier * de l'API. 
    Dans ce fichier, 
    - importer pytest et le module à tester au début de chaque fichier de test
        ```
        import os
        import sys
        __workdir__ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        __j2ldir__ = os.path.join(__workdir__, "src", "api")
        sys.path.append(__workdir__)
        sys.path.append(__j2ldir__)

        from src.api.votrejeu import *
        import pytest
        ...
        ```
    - definir une fonction "test_{featureATester}" en listant les assert
        ```
        def test_instanciation():
            player = VotreJeu("agentTest", "")
            assert player.life == 100
        ```

3. Utiliser pytest pour générer une série de test unitaires dans le dossier tests
    - Installer pytest
    ```
    pip install pytest
    ```
    - Executer pytest
    ```
    pytest path/vers/votreFichierDeTest.py -v -s
    ```
4. Implémenter les méthodes de votre classe concrête de votre Jeu en TDD
    - reprendre d'abord les méthodes qui wrappent pytactX
    - implémenter ensuite les features plus originales qui ne sont pas implémentées dans PytactX

4. Commit une fois 1 test passé par feature.
    Mentionner la référence (e.g. "100% pass #10 feature") à la carte feature dans votre kanban
    Sous trello, installer le power-ups "Card Numbers by Reenhanced" pour voir les numéro de chaque carte

5. Pour les plus avancés, intégrer pytest en CI/CD à chaque commit (pre-commit)

# 💻 Dev de votre server

1. A partir du tutoriel tutos.jusdeliens.com  "Créer vos propres règles du jeu"
- Téléchargez le dernier zip pytactx 
- Créer votre main.py dans votre dossier server recopiez le sample de l'arbitre pour comprendre les règles du jeu  

2. Nommer votre arbitre dans votre .env (NE PAS LE COMMIT):
```
@arenaname  
```
**arenaname** à remplacer par le nom de l'arène
ex: @spythoon pour l'arène spythoon

3. Utiliser les méthodes **ruleArena** et **rulePlayer** en bac à sable pour tester le bon fonctionnement des modifications du serveur
    - Redemarrer l'arène
    ```python
    arbiter.ruleArena("reset", True)
    ```
    - Modifier le infinite ammo de tous les joueurs par défaut (profile = 0)
    ```python
    infiniteAmmoRule = arbiter.game["infiniteAmmo"]
    infiniteAmmoRule[0] = True #Modifie uniquement pour le 1er porfile (0)
    arbiter.ruleArena("infiniteAmmo", infiniteAmmoRule)
    arbiter.update()
    ```
    - Créer des joueurs dans différentes équipes à différentes positions sur la carte
    ```python
    agents = {
        "joueur1": {
            "team": 0,
            "x": 5,
            "y": 10
        },
        "joueur2": {
            "team": 1,
            "x": 15,
            "y": 10
        },
        "ball": {
            "playerId": "",
            "profile": 4,
            "x": 15,
            "y": 10
        }
    }
    for agentId, attributes in agents.items():
        for attributeKey, attributeValue in attributes.items():
            arbitre.rulePlayer(agentId, attributeKey, attributeValue)
    arbiter.update()
    ```

4. Développer en CDD la logique de votre server dans votre main.py
```python
#0. Reset de l'arène
#1. Initialiser les règles du jeu : changer graphiques, et logiques, profiles des joueurs ...
#2. Créer les agents avec le bon profile et les bons états
#3. Fermer l'arène pour interdire la venue de nouveaux agents non autorisés
#4. Dans votre boucle principale : tant que le jeu tourne
    #4.1. Récupérer les requêtes et infos des joueurs dans le range de l'arbitre
    #4.2. Si le range change (ex: nFire pour check si un agent à tiré), 
        # 4.3. mettre à jour les règles du jeu (ex: appliquer acceleration sur agent, ou changer état de la map)
    #4.5. Sauvegarder le nouveau range avant de reboucler
    #4.6. Gérer condition de fin de jeu : fin du délai réglementaire, morts des joueurs d'une équipe ...
```