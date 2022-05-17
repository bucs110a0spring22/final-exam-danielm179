import requests
import json

class MakeApiCall_second:
  '''
  the class object for the first proxy class.
  functions
  N/A
  '''
  api_url_two = "https://api.web3.storage/upload"
  
  def get_data(self,api):
    '''
    setting definition for the function in order to retreive the wanted data from the api
    the arguments here are parameters for the function
    the returns are of the json class as well as str
    '''
    response = requests.get(api_url_two)
    if response.status_code == 200:
      print("data fetched succesfully ")
    else:
      print("{response.error_code} error with request ")

  def get_user_data(self, api, parameters):
    '''
    the purpose of this function was to input more specific parameters in order to find specific user data in the api
    the arguments here are parameters for the function
    the returns are of the str class that show us the results of our data search
    '''
    response = requests.get(api_url_two, params = parameters)
    if response.status_code == 200:
      print("data fetched succesfully ")
    else:
      print("{response.error_code} error with request ")

  def api_url(self, name):
    '''
    the purpose of this function was to give the api url being used a hard code into the function description
    '''
    self.name = "https://api.web3.storage/upload"

  def get(self):
    '''
    the purpose of this function was to give the api a set self description and to attain information from it
    '''
    self.get_data("https://api.web3.storage/upload")

  
  def __init__(self, api):
    '''
    the purose of this was to initialize the data structures that are required in the rest of the code
    the two parameters were of classes that are used to initialize these structures to a singular name
    the returns were used to describe these parameters
    '''
    self.get_data(api)

    parameters = {
      "year":"cloud"
    }
    self.get_user_data(self, api)

  def __str__(self, name):
      '''
    this is used in order to initialize the name of the class and apply it to the function so that it may be correctly called
    '''
      self.name = "MakeApiCall_second"



  if __name__ == "__main__":
    api_call = MakeApiCall_second("https://api.web3.storage/upload")