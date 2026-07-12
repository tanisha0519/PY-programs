import requests
import re
ip=input("Enter IP address:")
url=f"https://ipinfo.io/json/{ip}"
response=requests.get(url)
data=response.json()
print(data)
