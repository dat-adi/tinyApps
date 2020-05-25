import requests
import json

game_link = "https://api.crackwatch.com/api/games?page=1"
response = requests.get(game_link)
print(response.txt)