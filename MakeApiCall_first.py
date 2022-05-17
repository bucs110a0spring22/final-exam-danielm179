import requests
import json

class MakeApiCall_first:
  '''
  the class object for the first proxy class.
  functions
  N/A
  '''
  api_url = "https://api.helium.io/v1/stats"

  def get_data(self,api):
    '''
    setting definition for the function in order to retreive the wanted data from the api
    the arguments
    '''
    response = requests.get(api_url)
    if response.status_code == 200:
      print("data fetched succesfully ")
      self.formatted_print(response.json())
    else:
      print("{response.error_code} error with request ")

  def get_user_data(self, api, parameters):
    response = requests.get(api_url, params = parameters)
    if response.status_code == 200:
      print("data fetched succesfully ")
    else:
      print("{response.error_code} error with request ")

  def api_url(self, name):
    self.name = "https://api.helium.io/v1/stats"

  def get(self):
    self.get_data("https://api.helium.io/v1/stats")

  def formatted_print(self, obj):
    text = json.dumps(obj, sort_keys = TRUE)
    print(text)
    

  def __init__(self, api):
    self.get_data(api)

    parameters = {
      "year":"amount"
    }
    self.get_user_data(self, api)

  def __str__(self, name):
    #self.name = 



    if __name__ == "__main__":
      api_call = MakeApiCall_first("https://api.helium.io/v1/stats")