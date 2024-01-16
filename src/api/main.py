import j2l.pytactx.agent as pytactx
import enterzezone
import time

new_player = enterzezone.Player("joueur1", "enterzezone", "demo", "demo",
                                "mqtt.jusdeliens.com")
new_player1 = enterzezone.Player("joueur4", "enterzezone", "demo", "demo",
                                 "mqtt.jusdeliens.com")
new_player2 = enterzezone.Player("joueur3", "enterzezone", "demo", "demo",
                                 "mqtt.jusdeliens.com")
new_player3 = enterzezone.Player("joueur2", "enterzezone", "demo", "demo",
                                 "mqtt.jusdeliens.com")

new_player1.moveTowards(20, 25)
time.sleep(2)
new_player1.updateSelf()

new_player2.moveTowards(20, 25)
time.sleep(2)
new_player2.updateSelf()

new_player3.moveTowards(20, 25)
time.sleep(2)
new_player3.updateSelf()

new_player.moveTowards(7, 21)
time.sleep(2)
new_player.updateSelf()
time.sleep(2)
new_player.moveTowards(13, 14)
time.sleep(2)
new_player.updateSelf()
new_player.placeBlock()
i = 14
for i in range(26):
	time.sleep(0.5)
	new_player.moveTowards(i, 14)
	new_player.placeBlock()
	new_player.updateSelf()
new_player.moveTowards(30, 14)
time.sleep(2)
new_player.updateSelf()
while True:
	new_player.moveTowards(37, 14)
	new_player.updateSelf()
	time.sleep(5)
	new_player.moveTowards(38, 14)
	new_player.updateSelf()
