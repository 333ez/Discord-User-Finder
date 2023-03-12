import requests, json, time

token = "" # Token utilizado para o scan
user = input("[USERNAME] ") # Username do destinatário
rate = 30 # Delay

headers = {
    "Authorization" : token,
    "Content-Type": "application/json"
}
for n in range(1, 10000):
  data = {
    "username": user,
    "discriminator": n
  }
  r = requests.post("https://discord.com/api/v9/users/@me/relationships", headers=headers, json=data)
  if "401: Unauthorized" in r.text:
    quit("[TOKEN] Inválido")
  if "No users with DiscordTag exist" not in r.text:
    print(f"[#{str(n).zfill(4)}]", ">", '{"message": "User with DiscordTag exists", "code": 0}')
    quit()
  else:
    print(f"[#{str(n).zfill(4)}] > {r.text}")
  time.sleep(rate)