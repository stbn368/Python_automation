import requests
import json
import unittest

class TestGetRequest(unittest.TestCase):
    def test_get_request(self):
        url = "https://postman-echo.com/post"

        payload = json.dumps({
        "firstName": "Esteban",
        "secondName": "Calderón",
        "age": 32
        })
        headers = {
        'Content-Type': 'application/json',
        'Cookie': 'sails.sid=s%3AKsmfxt57chNKaoWQTI2Qcjylnj2e8rmI.Z4XdaERJoHf3XwxUbcGysqeHqkSpyuEumD6jRgBNzws'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        
        assert response.status_code == 200, "Status code is not 200"

if __name__ == "__main__":
    unittest.main()