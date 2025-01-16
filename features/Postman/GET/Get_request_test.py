import requests

url = "https://postman-echo.com/get?param1=value1&param2=value2"

payload = {}
headers = {
  'Cookie': 'sails.sid=s%3AF61UiSwytRpSXAkBXLo0vqlRv8UClkks.k2cUowuDmh3Rk%2B3aSA3cPqiXNwZvw0gLghrp%2BgzPLa4'
}

response = requests.request("GET", url, headers=headers, data=payload)

#print(dir(response))

assert response.status_code == 200, "Status code is not 200"