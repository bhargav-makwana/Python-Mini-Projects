import random as r
sport = input("What's your favourite sport? ")
team = input("What's your favourite " + sport + " team? ")
name = input("What's your name? ")

# Printing a nice message
print('\n---------------------------------------')
print('Oh wow! You are a true fan of '+ team.upper())
print(name.upper() + '? That sounds a nice name.')
print("so " + name.upper() + ", your lucky jersey number is:", r.randint(1,100))
print('-----------------------------------------')