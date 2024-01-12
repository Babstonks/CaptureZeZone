# import of standard libraries
import time
import os
import json
from referee import Referee

# File directory definition
__fileDir__ = os.path.dirname(os.path.abspath(__file__))

ARBITRE=os.getenv('ARBITRE')
ARENA=os.getenv('ARENA')
USERNAME=os.getenv('USERNAME')
PASSWORD=os.getenv('PASSWORD')
SERVER=os.getenv('SERVER')

# # Referee creation
# referee = pytactx.Agent(ARBITRE, ARENA, USERNAME, PASSWORD, SERVER, PORT)
referee = Referee(ARBITRE, ARENA, USERNAME, PASSWORD, SERVER)
referee.printInfoToArena("⌛ Initialisation de l'arbitre...")

serverRulesdict = {}

# # Reset arena
# referee.openArena(True)
referee.printInfoToArena("⌛ Reset de la map")
referee.update()
referee.resetArena()
referee.update()
time.sleep(3)
referee.update()




referee.printInfoToArena("⌛ Chargement des rules ...")
referee.update()

try:
    with open(os.path.join(__fileDir__, 'serverRules.json'), encoding='utf-8') as json_data:
         serverRulesdict = json.load(json_data)
except Exception as e:
    print(f"Une erreur est survenue dans le chargement des données : {e}")

referee.setArenaRules(serverRulesdict)
referee.update()
time.sleep(0.3)

referee.createPlayers(serverRulesdict)
referee.update()
time.sleep(0.3)

referee.printInfoToArena("⌛ En attente des joueurs ...")
referee.update()
time.sleep(9)
 
readyPlayers = []

while len(readyPlayers) < len(referee.getCurrentRange()):
    referee.update()
    time.sleep(0.3)
    for player in referee.getCurrentRange().values():
        if not player["idle"]:
            if player["clientId"] not in readyPlayers :
                readyPlayers.append(player["clientId"])
    print(readyPlayers)

referee.printInfoToArena("Jouez !! ")
referee.update()

# # Launch party msg
referee.printInfoToArena("🟢 C'est parti !")
referee.update()
time.sleep(2)

while (True):
    referee.update()
    referee.rotate((referee.getDir()+1)%4)
    for player in referee.getCurrentRange().values():
        if not player["idle"]:
            if player["led"][1] == 3 :
                print(player)
                referee.placeBlock(player)
                

##while not referee.isGameOver() :
    # #  referee direction changes to apply updates
   ## print("test")
    ## vb referee.rotate((referee.getDir()+1)%4)