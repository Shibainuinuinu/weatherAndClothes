import requests
from clothespiece import r
from config import yelpFusionAPIKey

def stores(random_clothing_item):
  print("--------------------------------------------")
  print(f"Clothing item - {random_clothing_item}")
  print(" ")
  # Set up API endpoint and parameters
  url = 'https://api.yelp.com/v3/businesses/search'
  #set up auhtorization with API key. Use headers dictionary with key as 'Authorization'
  #and value as 'Bearer <API key>'
  #Custom HTTP headers are additional HTTP headers that can be added to an HTTP request or response to provide extra information e.g API key 
  headers = {'Authorization': f'Bearer {yelpFusionAPIKey} '}
  #query parameters to be included in the url 
  params = {'term': random_clothing_item, 'location': 'San Francisco'}
  
  # Send HTTP request w/Yelp Fusion URL, API key, and params of SF & clothing item
  response = requests.get(url, headers=headers, params=params)

  # Converts JSON to a dictionary 
  data = response.json()
  businesses = data['businesses']
  
  #Print store name, ratings, price, and location 
  for business in businesses:
      if 'price' in business:
        print(f"{business['name']} - {business['rating']} stars  - {business['price']} -{business['location']['address1']}")
      else:
        print(f"{business['name']} - {business['rating']} stars")

#gives a set of stores for each item in the clothing suggestions
for clothingItem in r:
  stores(clothingItem)
  