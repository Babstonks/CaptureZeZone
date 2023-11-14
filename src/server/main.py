# import of standard libraries
import time
import os
import json

# File directory definition
__fileDir__ = os.path.dirname(os.path.abspath(__file__))

# ENV variables config
from dotenv import load_dotenv
load_dotenv()
ARBITRE=os.getenv('ARBITRE')
ARENA=os.getenv('ARENA')
USERNAME=os.getenv('USERNAME')
PASSWORD=os.getenv('PASSWORD')
SERVER=os.getenv('SERVER')

# # Import referee class and utils
from referee import Referee
from utils import *

# # Import json rules file
# Try catch to retrieve rules data
try:
    with open(os.path.join(__fileDir__, 'serverRules.json')) as json_data:
        serverRulesdict = json.load(json_data)
except Exception as e:
    print(f"Une erreur est survenue dans le chargement des données : {e}")

# # Referee creation
# referee = pytactx.Agent(ARBITRE, ARENA, USERNAME, PASSWORD, SERVER, PORT)
referee = Referee(ARBITRE, ARENA, USERNAME, PASSWORD, SERVER, PORT, DURATION)
referee.printInfoToArena("⌛ Initialisation de l'arbitre...")