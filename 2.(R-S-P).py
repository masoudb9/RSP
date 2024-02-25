import random
user_score = 0
pc_score = 0
m = 0
while m == 0:
    my_list = ['rock', 'paper', 'scissor']
    ga = random.choice(my_list)
    g2 = input('User turn: ')
    if g2 == 'rock' and ga == 'scissor':
        user_score = user_score + 1
        print('user score:', user_score)
        print('user won')
    elif g2 == 'rock' and ga == 'paper':
        pc_score = pc_score + 1
        print('pc score:', pc_score)
        print('pc won')
    elif g2 == 'paper' and ga == 'rock':
        pc_score = pc_score + 1
        print('pc score:', pc_score)
        print('pc won')
    elif g2 == 'paper' and ga == 'scissor':
        pc_score = pc_score + 1
        print('pc score:', pc_score)
        print('pc won')
    elif g2 == 'scissor' and ga == 'paper':
        user_score = user_score + 1
        print('user score:', user_score)
        print('user won')
    elif g2 == 'scissor' and ga == 'rock':
        pc_score = pc_score + 1
        print('pc score:', pc_score)
        print('pc won')
    elif ga == g2:
        print('equal try again'.title())
    elif g2 != my_list:
        print('invalid input, try  again.'.title())
    elif user_score == 5:
        print('game over')
        start = input("do you want to play again?  yes/no")
        break
    elif pc_score == 5:
        print('game over')
        break





