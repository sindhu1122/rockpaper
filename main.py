from random import choice
rules={'rock':'paper','scissors':'rock','paper':'scissors'}
ch=['rock','paper','scissors']
while(1):
  print("enter your choice")
  h=input()
  c=rules[choice(ch)]
  if h=='exit' or h=='quit':
    break
  elif h in rules:
    ch.append(h)
    print("computer selected",c)
    if rules[c]==h:
      print("You win")
    elif rules[h]==c:
      print("Computer won")
    else:
      print("Tie")
  else:
    print("Wrong choice")


