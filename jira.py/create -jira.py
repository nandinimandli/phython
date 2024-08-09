# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests # type: ignore
from requests.auth import HTTPBasicAuth # type: ignore
import json

url = "https://.atlassian.net/rest/api/3/project"

API_TOKEN=""
auth = HTTPBasicAuth("Email ", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)

name = output[0]["name"]

print(name)