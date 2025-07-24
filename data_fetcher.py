import requests
from dotenv import load_dotenv
import os

def fetch_data(animal_name):
  """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary:
  {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
  },
  """
  load_dotenv()
  api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(animal_name)
  response = requests.get(api_url, headers={'X-Api-Key': os.getenv('X_API_KEY')})
  if response.status_code == requests.codes.ok:
      print(response.text)
  else:
      print("Error:", response.status_code, response.text)
  return response.text