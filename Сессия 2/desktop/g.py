import requests

api_personal = "http://127.0.0.1:8000/api/v1/personal/"

last_name = "dfgdfeg" 
response = requests.get(f"{api_personal}")
data = response.json()
account = data["objects"]

# print(account)
for value in account:
  for key, values in value.items():
      print(f"{key}: {values}")