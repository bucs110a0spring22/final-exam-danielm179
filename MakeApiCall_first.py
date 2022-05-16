import requests


class MakeApiCall_first:
  def get_data(self,api):
    response = requests.get("{api}")
    if response.status_code == 200:
      print("data fetched succesfully ")
    else:
      print("{response.error_code} error with request ")

  def get_user_data(self, api, parameters):
    response = requests.get("{api}", params = parameters)
    if response.status_code == 200:
      print("data fetched succesfully ")
    else:
      print("{response.error_code} error with request ")

  def api_url(self, name):
    self.name = "https://api.helium.io/v1/stats"

  def get(self):
    self.get_data("https://api.helium.io/v1/stats")
    


  def __init__(self, api):
    self.get_data(api)

    parameters = {
      "data":"weather"
    }
    self.get_user_data(self, api)



if __name__ == "__main__":
  api_call = MakeApiCall_first("https://api.helium.io/v1/stats")