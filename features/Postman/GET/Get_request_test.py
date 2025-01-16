import unittest
import requests

class TestGetRequest(unittest.TestCase):
    def test_get_request(self):
      url = "https://postman-echo.com/get?param1=value1&param2=value2"
      payload = {}
      headers = {
          'Cookie': 'sails.sid=%3AF61UiSwytRpSXAKBXL0oVqjRv8UClkks.k2UowuDmh3Rk%2B3aSA3cPqiXNvZw0gLghrp%2BgzPL4a'
      }

      response = requests.request("GET", url, headers=headers, data=payload)
      
      #print(dir(response))
      
      # Aserción para verificar el código de estado
      self.assertEqual(response.status_code, 200, "Status code is not 200")
      
    def test_get_with_id(self):
      url = "https://postman-echo.com/get?id=1"
      payload = {}
      headers = {
        'Cookie': 'sails.sid=s%3AKsmfxt57chNKaoWQTI2Qcjylnj2e8rmI.Z4XdaERJoHf3XwxUbcGysqeHqkSpyuEumD6jRgBNzws'
      }

      response = requests.request("GET", url, headers=headers, data=payload)

      self.assertEqual(response.status_code, 200, "Status code is not 200")

if __name__ == "__main__":
    unittest.main()
