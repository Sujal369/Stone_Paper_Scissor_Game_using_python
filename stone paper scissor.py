import random
print("enter your move")
input = input()
a = ['stone', 'paper', 'scissor']
s = random.randrange(len(a))
b = a[s]
if b == input:
    print("The game is tie")
elif b == 'stone' and input == 'paper':
    print("you won with paper and computer lost with stone")
elif b == 'paper' and input == 'stone':
    print("you lost with stone and computer win with paper")
elif b == 'stone' and input == 'scissor':
    print("you lost with scissor and computer win with stone")
elif b == 'scissor' and input == 'stone':
    print("you win with stone and computer lost with scissor")
elif b == 'paper' and input == 'scissor':
    print("you won with scissor and computer lost with paper")
elif b == 'scissor' and input == 'paper':
    print("you lost with paper and computer with with scissor")
