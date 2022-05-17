import requests
import json
import MakeApiCall_first
import MakeApiCall_second


def main():
  '''
  This is the main driver code. It is used to take the api's and find the similar number of class models between the two so that we can understand if these two api's would work well together in data manipulation in blockchain work
  N/A
  returns here are both str and int types
  '''
  
  api_url_one = "https://api.helium.io/v1/stats"
  api_url_two = "https://git.0x0.st/mia/0x0"
  
  response_one = requests.get(api_url_one)
  if response_one.status_code == 200:
    print(response_one.content)
  
  response_two = requests.get(api_url_two)
  if response_two.status_code == 200:
    print(response_two.content)

  for item in MakeApiCall_first('class'):
    return item
    item = item_one
    print("these are the classes found in this blockchain file" + str(item_one))
    
  for item in MakeApiCall_second('class'):
    return item
    item = item_two
    print("these are the classes found throughout this cloud file" + str(item_two))

  while item_one == item_two:
    item_list = list(item_one, item_two)
    item_count = len(item_list)
    return item_count
    print("This is how many similar classes are found throughout blockchain and cloud files in this specific case: " + str(item_count) + "This shows us the strong positive relationship found between these programs and gives us reason to be willing to relate these to one another. ")
  

main()