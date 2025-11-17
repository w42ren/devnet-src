# Fill in this file with the people listing code from the Webex Teams exercise
import requests
import json

access_token = ''
url = 'https://webexapis.com/v1/people'
person_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vZTY0ZTZhMDAtYTI5OS0xMWYwLTg1MTctZWJmZDE5N2Y0NmZm'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {
    'email': 'user@example.com'
}
res = requests.get(url, headers=headers, params=params)
print(json.dumps(res.json(), indent=4))

