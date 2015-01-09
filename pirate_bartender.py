import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
  } 

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

def styleOfDrink():  # Create a drink preferences dictionary and return it
    responses = {}
    for question in questions:
        print questions[question]
        response = str(raw_input())
        print " "
        if response == 'yes' or response == 'y':
            responses[question] = True
        else:
            responses[question] = False            
    return responses

def constructDrink(preferences):  # Create a drink based on choice of drinks a customer like
    drink = []
    for i in preferences:
        if preferences[i] == True:
            drink.append(random.choice(ingredients[i]))
    return drink

def main():
    preference = styleOfDrink()
    beverage = constructDrink(preference)
    print "Your Beverage is coming up."
    print "Your choice is"
    for i in beverage:
        print "A {}".format(i)

if __name__ =="__main__":
    main()
 