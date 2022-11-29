import sys
import requests
import socket
import json

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <url>")
    sys.exit(1)

req = requests.get(f"https://{sys.argv[1]}")
print(f"\n {str(req.headers)}")

gethostby = socket.gethostbyname((sys.argv[1]))
print(f"\nThe IP address of  {sys.argv[1]} is:  {gethostby} \n")

#ipinfo.IOError

req_two = requests.get("https://ipinfo.io/"+ gethostby+"/json")
resp = json.loads(req_two.text)

print(f"Location:  {resp['loc']}")
print(f"Region:  {resp['region']}")
print(f"City:  {resp['city']}")
print(f"Country:  {resp['country']}")