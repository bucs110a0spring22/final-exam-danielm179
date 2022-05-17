import requests
import json

class MakeApiCall_second:
  api_url_two = "https://api.web3.storage/upload"
  
  def get_data(self,api):
    response = requests.get(api_url_two)
    if response.status_code == 200:
      print("data fetched succesfully ")
    else:
      print("{response.error_code} error with request ")

  def get_user_data(self, api, parameters):
    response = requests.get(api_url_two, params = parameters)
    if response.status_code == 200:
      print("data fetched succesfully ")
    else:
      print("{response.error_code} error with request ")

  def api_url(self, name):
    self.name = "https://api.web3.storage/upload"

  def get(self):
    self.get_data("https://api.web3.storage/upload")

  
  def __init__(self, api):
    self.get_data(api)

    parameters = {
      "year":"cloud"
    }
    self.get_user_data(self, api)



if __name__ == "__main__":
  api_call = MakeApiCall_second("https://api.web3.storage/upload")