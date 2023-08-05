from main import temperature_f

def clothing_rec(temperature):
  if temperature < 50:
        clothing_rec = ['heavy coats', 'gloves', 'hats', 'scarves', 'boots', 'turtle necks', 'hoodies', 'cardigan', 'beanies']
  elif temperature < 75:
        clothing_rec = ['light jackets', 'sweaters', 'jeans', 'bucket hats', 'sneakers', 'sun hats']
  elif temperature < 80:
        clothing_rec = ['t-shirts', 'shorts', 'sandals', 'sunglasses']
  else:
        clothing_rec = ['shorts', 'tank tops', 'sundresses', 'sunglasses']
  return clothing_rec 

temperature = temperature_f
r = clothing_rec(temperature)
recommendations = ', '.join(clothing_rec(temperature))
print("According to the weather today, here is a list of  what you can wear or add to your outfit: \n" + recommendations)
print(" ")
#prints out clothing type recommendations 


