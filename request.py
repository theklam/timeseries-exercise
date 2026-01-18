import requests

resp = requests.get("https://api.github.com/repos/psf/requests")
data = resp.json()

print(data["stargazers_count"])
