import random

def play():
  user = input("Rock papper scisoors shot \n'r' for rock, 'p' for paper, 's' for scissors. ")
  computer = random.choice(['r', 'p', 's'])
  if user == computer:
    return 'it is a tie'


  # r beats s, s beats p, p beats r
  elif is_win(user, computer):
    return ' you win'
  else:
    return ' you lost'




def is_win(player, opponent):
  # r beats s, s beats p, p beats r
  if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
    return true
user= " "

while user != "stop":
  print (play())

