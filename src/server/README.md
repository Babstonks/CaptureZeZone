# Referee Class

The `Referee` class is a Python class designed to facilitate interactions between a game referee and a gaming environment. It is designed to work with the `pytactx` module for communication with the gaming server.

## Overview

The `Referee` class acts as a bridge between the game referee and the gaming environment. It provides methods to update game information, set arena rules, create players, and perform various actions within the game environment.

Methods
### update()
Fetch the last values of referee data from the server and send buffered requests in one shot to limit bandwidth. This method should be called in the main loop at least every 10 milliseconds.

### getDir() -> int
Return the referee direction.

### rotate(dir: int) -> None
Request a rotation of the agent on the grid. Dir should be integers values from 0 (east) to 3 (south). The request will be sent in the next update() call.

### getGameInfos() -> dict[str, Any]
Request game information.

### setArenaRules(rulesFile: dict[str, Any]) -> None
Define all the rules of the arena based on a file.

### createPlayers(rulesFile: dict[str, Any]) -> None
Create all arena players based on the rules file.

### printInfoToArena(info: str) -> None
Print the input string to the arena info area.

### openArena(open: bool) -> None
Close arena so no other player can join.

### resetArena() -> None
Reset the entire arena.

### resetMap() -> None
Reset the status of all map tiles.

### getRefereeMap() -> [[int]]
Return referee map value.

### updateRefereeMap(x: int, y: int, value: int) -> None
Update the referee map.

### updateArenaMap(map: [[int]]) -> None
Update the arena map with the referee copy.

### getCurrentRange() -> dict[str, Any]
Retrieve the current range of the referee from the server.

### setPlayerProfileOnFire(player: dict[str, Any]) -> None
Set the player profile depending on if it is firing or not.

### decreasePlayerAmmo(player: dict[str, Any]) -> None
Update player ammo on each shot.

### getCurrTimestamp() -> int
Retrieve the current timestamp from the server.

### isGameOver() -> bool
Return true if the game is over, depending on specific conditions.

### isBlockPlacable(player: dict[str, Any]) -> bool
Call placeBlock and return True if the player can place a block, False otherwise.

### placeBlock(player: dict[str, Any]) -> None
Place a block on the arena.

## Contributing
Contributions are welcome! Feel free to open issues or pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.


