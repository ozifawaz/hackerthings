import requests

game_pin = input("gamepin: ")
name = input("player to kick: ")

headers = {
	"Referer": "https://www.blooket.com"
}

r = requests.delete(f"https://api.blooket.com/api/firebase/client?id={game_pin}&name={name}", headers=headers)

if r.status_code == 200:
	print(f"Kicked {name} from game {game_pin}")
else:
	print(f"Failed to kick {name} because of error code: {str(r.status_code)}")
