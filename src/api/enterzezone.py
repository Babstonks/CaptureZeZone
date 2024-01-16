import j2l.pytactx.agent as pytactx


class IPlayer:

	def getTeam(self) -> int:
		"""
		Return team number
		"""
		...

	def getCoordinates(self) -> tuple[int, int]:
		"""
		Return the actual coordinates x and y
		"""
		...

	def getDirection(self) -> int:
		"""
		Return the player direction
		"""
		...

	def placeBlock(self) -> bool:
		"""
		Place a block in front of u
		"""
		...

	def move(self) -> bool:
		"""
		Move the player once
		"""
		...

	def moveTowards(self, x, y) -> bool:
		"""
		Move the player once
		"""
		...

	def shoot(self) -> bool:
		"""
		Start shooting with a range of 1 block
		"""
		...

	def spawn(self) -> bool:
		"""
		Spawn the player in the closest spawn point
		"""
		...

	def updateSelf(self) -> bool:
		"""
		Spawn the player in the closest spawn point
		"""
		...

	def rotate(self, dir: int) -> None:
		"""
		Request a rotation of the agent on the grid.
		Dir should be integers values from 0 (east) to 3 (south).
		The request will be send the next update() call
		"""
		...


class Player(IPlayer):

	def __init__(self,
	             playerId: str or None = None,
	             arena: str or None = None,
	             username: str or None = None,
	             password: str or None = None,
	             server: str or None = None,
	             port: int = 1883,
	             verbosity: int = 2) -> None:
		self.__agent = pytactx.Agent(playerId, arena, username, password, server,
		                             port, verbosity)

	def placeBlock(self):
		self.__agent.setColor(self.__agent.color[0], 3, self.__agent.color[2])

	def getTeam(self):
		self.__agent.team

	def moveTowards(self, x, y) -> bool:
		self.__agent.moveTowards(x, y)

	def updateSelf(self):
		self.__agent.update()


def getDirection(self):
	return self.__agent.dir


def getCoordinates(self) -> tuple[int, int]:
	return (self.__agent.x, self.__agent.y)


def rotate(self, dir: int):
	self.__agent.lookAt(dir)

def move(self):
	print(self.__agent.dir)
	match (self.__agent.dir):
			case 0:
					self.__agent.move(1, 0)
			case 1:
					self.__agent.move(0, -1)
			case 2:
					self.__agent.move(-1, 0)
			case 3:
					self.__agent.move(0, 1)


class TestPlayerMethods():

	def test_placeBlock(self):
			self.player.placeBlock()
			assert self.player._Player__agent.color[1] == 3

	def test_moveTowards(self):
			self.player.moveTowards(1, 2)
			assert self.player._Player__agent.getCoordinates() == (1, 2)

	def test_getCoordinates(self):
			self.player._Player__agent.x = 3
			self.player._Player__agent.y = 4
			result = self.player.getCoordinates()
			assert result == (3, 4)
-
