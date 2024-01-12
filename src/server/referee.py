from typing import Any
import time
from math import cos,sin,pi
# from utils import *

import j2l.pytactx.agent as pytactx


# Referee interface
class IReferee:
    def update(self) -> None:
        """
        Fetch the last values of referee data from server
        And send buffered requests in one shot to limit bandwidth.
        To be call in the main loop at least every 10 msecs.
        """
        ...

    def getDir(self) -> int:
        """
        return referee direction
        """
        ...

    def rotate(self, dir: int) -> None:
        """
        Request a rotation of the agent on the grid.
        Dir should be integers values from 0 (east) to 3 (south).
        The request will be send the next update() call
        """
        ...

    def getGameInfos(self) -> dict[str, Any]:
        """
        Request game infos
        """
        ...

    def setArenaRules(self, rulesFile: dict[str, Any]) -> None:
        """
        Define all the rules of the arena based on a file
        """
        ...

    def createPlayers(self, rulesFile: dict[str, Any]) -> None:
        """
        Create all arena players based on the rules file
        """
        ...

    def printInfoToArena(self, info: str) -> None:
        """
        Print the input string to the arena info area
        """
        ...

    def openArena(self, open: bool) -> None:
        """
        Close arena so no other player can join
        """
        ...

    def resetArena(self) -> None:
        """
        Reset the entire arena
        """
        ...

    def resetMap(self) -> None:
        """
        Reset status of all map tiles
        """

    def getRefereeMap(self) -> [[int]]:
        """
        return referee map value
        """
        ...

    def updateRefereeMap(self, x: int, y: int, value: int) -> None:
        """
        update the referee map
        """
        ...

    def updateArenaMap(self, map: [[int]]) -> None:
        """
        Update the arena map with the referee copy
        """
        ...

    def getCurrentRange(self) -> dict[str, Any]:
        """
        retrieve the current range of the referee from the server
        """
        ...

    def setPlayerProfileOnFire(self, player: dict[str, Any]) -> None:
        """
        set the player profile depending on if it is firing or not
        """
        ...

    def decreasePlayerAmmo(self, player: dict[str, Any]) -> None:
        """
        Update player ammo on each shoot
        """
        ...

    def getCurrTimestamp(self) -> int:
        """
        Retrieve current timestamp from the server
        """
        ...

    def isGameOver(self) -> bool:
        """
        Return true if game is over, depending on specific conditions
        """
        ...
    
    def isBlockPlacable(self, player: dict[str, Any]) -> bool:
      """
      Call placeBlock and return True if the player can place a block, False otherwise
      """
      ...

    def placeBlock(self, player) -> None:
      """
      Place a block on the arena
      """
      ...


class Referee(IReferee):
    def __init__(self, playerId: str or None = None, arena: str or None = None, username: str or None = None,
                 password: str or None = None, server: str or None = None, port: int = 1883,
                 roundDuration: int = 300) -> None:
        self.__pytactxAgent = pytactx.Agent(playerId, arena, username, password, server, port)

        self.__pytactxAgent.team = 0
        self.__pytactxAgent.profile = 2
        self.__map = self.__pytactxAgent.game["map"]

        self.__empty = 2
        self.__plateform = 7

        while len(self.__pytactxAgent.game) == 0:
            self.__pytactxAgent.lookAt((self.__pytactxAgent.dir + 1) % 4)
            self.__pytactxAgent.update()

    def update(self) -> None:
        time.sleep(0.3) 
        self.__pytactxAgent.update()

    def getDir(self) -> int:
        return self.__pytactxAgent.dir

    def rotate(self, dir: int) -> None:
        self.__pytactxAgent.lookAt(dir)

    def getGameInfos(self) -> dict[str, Any]:
        return self.__pytactxAgent.game

    #A fusionner 

    def setArenaRules(self, rulesFile: dict[str, Any]) -> None:
        self.printInfoToArena("⌛ Définition des règles de la carte ...")
        for arenaRule, arenaAttribute in rulesFile["arenaRules"].items():
            if arenaRule == "map":
                self.__map = arenaAttribute
            self.__pytactxAgent.ruleArena(arenaRule, arenaAttribute)

    def createPlayers(self, rulesFile: dict[str, Any]) -> None:
        self.printInfoToArena("⌛ Création des joueurs ...")
        for player, playerAttributes in rulesFile["playersRules"].items():
            for attributeKey, attributeValue in playerAttributes.items():  
                self.__pytactxAgent.rulePlayer(player, attributeKey, attributeValue)

    def printInfoToArena(self, info: str) -> None:
        self.__pytactxAgent.ruleArena("info", info)

    def openArena(self, open: bool) -> None:
        self.__pytactxAgent.ruleArena("open", open)

    def resetArena(self) -> None:
        self.__pytactxAgent.ruleArena("reset", True)



    #def getRefereeMap(self) -> [[int]]:
    #    return self.__map

    #def updateRefereeMap(self, x: int, y: int, value: int) -> None:
    #    self.__map[y][x] = value

    def updateArenaMap(self) -> None:
        self.__pytactxAgent.ruleArena("map", self.__map)
        time.sleep(0.3)
        self.__pytactxAgent.update()

    #def getOldRange(self) -> dict[str, Any]:
    #    return self.__oldRange

    #def setOldRange(self, range: dict[str, Any]) -> None:
    #    self.__oldRange = range

    def getCurrentRange(self) -> dict[str, Any]:
        return self.__pytactxAgent.range

    def setPlayerProfileOnFire(self, player: dict[str, Any]) -> None:
        if self.getCurrentRange()[player["clientId"]]["nFire"] > self.getOldRange()[player["clientId"]]["nFire"]:
            self.__pytactxAgent.rulePlayer(player["clientId"], "profile", 1)
        else:
            self.__pytactxAgent.rulePlayer(player["clientId"], "profile", 0)

    def getTeamsScores(self) -> tuple[int, int]:
        return self.__scoreDealer.getTeamsScores()

    def updateScores(self, map: [[int]]) -> tuple[float, float]:
        return self.__scoreDealer.updateScores(map)

    def decreasePlayerAmmo(self, player: dict[str, Any]) -> None:
        self.__pytactxAgent.rulePlayer(player["clientId"], "ammo", player["ammo"] - 1)

    def startTimeMaster(self) -> None:
        self.__timeMaster.start()

    def getRemainingTime(self) -> int:
        return self.__timeMaster.getRemainingTime()

    def isGameOver(self) -> bool:
        if self.__timeMaster.getRemainingTime() <= 0:
            return True
        return False

    def isBlockPlacable(self, player: dict[str, Any]) -> bool:
        nextX = int(player["x"] + cos(player["dir"] * (pi/2)))
        nextY = int(player["y"] - sin(player["dir"] * (pi/2)))
        if nextX >= 0 and nextX < 40 and nextY >= 0 and nextY < 30:
          if self.getGameInfos()["map"][nextY][nextX] == self.__empty:
            return True
        return False

    def placeBlock(self, player: dict[str, Any]) -> None:
      if self.isBlockPlacable(player):
        nextX = int(player["x"] + cos(player["dir"] * (pi/2)))
        nextY = int(player["y"] - sin(player["dir"] * (pi/2)))
        self.__map[nextY][nextX] = self.__plateform
        self.updateArenaMap()
