import random

name = input('Enter your name : ')
print(f'All the best {name}')

goats = ['michael', 'sachin', 'ronaldo', 'messi', 'tiger', 'lewis', 'kobe', 'virat', 'saina', 'serena', 'rafael']
goat= random.choice(goats)

chances= len(goat)*2
print(f'You\'ll get {chances} chances.' )

count = 0
collection_choices = []
unique_char = set(goat)
while count < chances:
    choice = input('Enter the alphabet you want to choose : \n')
    if choice in goat:
        collection_choices.append(choice)
        if set(collection_choices) == unique_char:
            print(f'Hurray🥂🍾🎉 you won, the correct word is {goat}')
            break
        else:
            print('You are correct, proceed to next one 👍')
    elif choice not in goat:
        count+= 1
        print('You are incorrect, lets try again 😢\n')
if count == chances:
    print('Sorry you have completed your chances!!! Better luck next time 🤞🤞')
    