#TASK 5
def recipe_calculator():
    ingredients=['milk','flour','eggs','sugar']
    quantity=[200,250,3,100]
    serving=int(input("Enter the number of servings="))
    for i in range(len(quantity)):
        print(ingredients[i],'=',(quantity[i]*serving))

recipe_calculator()
