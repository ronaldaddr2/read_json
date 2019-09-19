import json,urllib.request
data = urllib.request.urlopen("https://api.github.com/users?since=100").read()
output = json.loads(data)
print (output)