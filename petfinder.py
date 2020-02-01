import requests
from secrets import API_ACCESS_TOKEN

resp = requests.get(
    "https://api.petfinder.com/v2/animals",
    params={"type": "Dog"},
    headers={f"Authorization": "Bearer {API_ACCESS_TOKEN}"}
)
breakpoint()

# resp.json()['animals'][0] --> gives first dog