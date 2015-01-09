def styleOfDrink():  # Create a drink preferences dictionary and return it
  questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
  } 
  responses = {}
  for question in questions:
    print questions[question]
    resp = str(raw_input())
    if resp == 'yes' or resp == 'y':
      responses[question] = True
    else:
      responses[question] = False
  return responses
def constructDrink(preferences):
  ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
    }
  drink = []
  for i in preferences:
    if preferences[i] == True:
        drink.append([i, ingredients[i]])
  return drink
if __name__ == '__main__':
  preference = styleOfDrink()
  print constructDrink(preference)




  
    
  
  