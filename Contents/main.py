import json

with open('config.json') as config_file:
    config = json.load(config_file)

api_key = config.get('API_KEY')

if api_key:
    print(f"Your API KEY is : {api_key}")
else:
    print("API Key is not Found.")