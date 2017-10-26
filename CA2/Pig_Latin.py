print 'welcome to pig latin'
pyg = 'ay'
original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
  print 'hereis your wors:', original
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:]
  print 'here is pig latin version', new_word
else:
  print 'empty'
  
  #################   Holidays cost
  
def hotel_cost(nights):
  return nights * 140
def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  else:
    city == "Los Angeles"
    return 475
def rental_car_cost(days):
  if days >= 7:
    return days * 40 - 50
  elif days >=3:
    return days * 40 - 20
  else:
    return days * 40
def trip_cost(city, days, spending_money):
  return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
print trip_cost("Los Angeles", 5, 600) 
    
    #################################